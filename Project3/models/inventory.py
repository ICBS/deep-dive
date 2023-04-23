from utils.validators import *


class Resource:

  def __init__(self, name: str, manufacturer: str, total: int, allocated: int):
    '''
        name: user-friendly name of resource instance (e.g.Intel Core i9-9900K)
        manufacturer: resource instance manufacturer (e.g. Nvidia)
        total: inventory total (how many are in the inventory pool)
        allocated: number allocated (how many are already in use)
        '''
    validate_int('total', total, 1)
    validate_int('allocated', allocated, min_val=0, max_val=total)
    self._name = name
    self._manufacturer = manufacturer
    self._total = total
    self._allocated = allocated

  @property
  def name(self):
    return self._name

  @property
  def manufacturer(self):
    return self._manufacturer

  @property
  def total(self):
    return self._total

  @property
  def allocated(self):
    return self._allocated

  @property
  def category(self):
    return type(self).__name__.lower()

  def __str__(self):
    return self.name

  def __repr__(self):
    return (f'{self.name} ({self.category} - {self.manufacturer}) : '
            f'total={self.total}, allocated={self.allocated}')

  def claim(self, n):
    try:
      validate_int('number', n, 1, self.total - self.allocated)
    except ValueError:
      raise ValueError('Cannot claim more than available.')
    self._allocated += n

  def freeup(self, n):
    try:
      validate_int('number', n, 1, self.allocated)
    except ValueError:
      raise ValueError('Cannot return more than allocated.')
    self._allocated -= n

  def died(self, n):
    self.freeup(n)
    self._total -= n

  def purchased(self, n):
    validate_int('number', n, 1)
    self._total += n


class CPU(Resource):

  def __init__(self, name: str, manufacturer: str, total: int, allocated: int,
               cores: int, socket: str, power_watts: int):
    super().__init__(name, manufacturer, total, allocated)
    validate_int('cores', cores, 1)
    validate_int('power_watts', power_watts, 1)
    self._cores = cores
    self._socket = socket
    self._power_watts = power_watts

  def __repr__(self):
    return f'{self.category}: {self.name} ({self.socket} - x{self.cores})'

  @property
  def cores(self):
    return self._cores

  @property
  def socket(self):
    return self._socket

  @property
  def power_watts(self):
    return self._power_watts


class Storage(Resource):

  def __init__(self, name: str, manufacturer: str, total: int, allocated: int,
               capacity_gb: int):
    super().__init__(name, manufacturer, total, allocated)
    validate_int('capacity_gb', capacity_gb, 1)
    self._capacity_gb = capacity_gb

  def __repr__(self):
    return f'{self.category}: {self.capacity_gb} GB'

  @property
  def capacity_gb(self):
    return self._capacity_gb


class HDD(Storage):

  def __init__(self, name: str, manufacturer: str, total: int, allocated: int,
               capacity_gb: int, size: str, rpm: int):
    super().__init__(name, manufacturer, total, allocated, capacity_gb)
    validate_int('rpm', rpm, 1000, 50000)
    self._size = size
    self._rpm = rpm

  def __repr__(self):
    s = super().__repr__()
    return f'{s} ({self.size}, {self.rpm} rpm)'

  @property
  def size(self):
    return self._size

  @property
  def rpm(self):
    return self._rpm


class SSD(Storage):

  def __init__(self, name: str, manufacturer: str, total: int, allocated: int,
               capacity_gb: int, interface: str):
    super().__init__(name, manufacturer, total, allocated, capacity_gb)
    self._interface = interface

  def __repr__(self):
    s = super().__repr__()
    return f'{s} ({self.interface})'

  @property
  def interface(self):
    return self._interface
