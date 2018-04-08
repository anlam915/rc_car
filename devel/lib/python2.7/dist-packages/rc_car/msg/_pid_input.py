# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rc_car/pid_input.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class pid_input(genpy.Message):
  _md5sum = "2455c9230edc930265906132ca470811"
  _type = "rc_car/pid_input"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 vel
float32 error
bool obstacle_flag"""
  __slots__ = ['vel','error','obstacle_flag']
  _slot_types = ['float32','float32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       vel,error,obstacle_flag

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(pid_input, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.vel is None:
        self.vel = 0.
      if self.error is None:
        self.error = 0.
      if self.obstacle_flag is None:
        self.obstacle_flag = False
    else:
      self.vel = 0.
      self.error = 0.
      self.obstacle_flag = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_2fB.pack(_x.vel, _x.error, _x.obstacle_flag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 9
      (_x.vel, _x.error, _x.obstacle_flag,) = _struct_2fB.unpack(str[start:end])
      self.obstacle_flag = bool(self.obstacle_flag)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_2fB.pack(_x.vel, _x.error, _x.obstacle_flag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 9
      (_x.vel, _x.error, _x.obstacle_flag,) = _struct_2fB.unpack(str[start:end])
      self.obstacle_flag = bool(self.obstacle_flag)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2fB = struct.Struct("<2fB")
