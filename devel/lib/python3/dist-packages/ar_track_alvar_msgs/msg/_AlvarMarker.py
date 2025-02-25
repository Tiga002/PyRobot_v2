# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ar_track_alvar_msgs/AlvarMarker.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg
import geometry_msgs.msg

class AlvarMarker(genpy.Message):
  _md5sum = "2cb98ba212070cd8fe95c2bdafca0cac"
  _type = "ar_track_alvar_msgs/AlvarMarker"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
uint32 id
uint32 confidence
geometry_msgs/PoseStamped pose
geometry_msgs/PoseStamped pose_img_0
geometry_msgs/PoseStamped pose_img_1
geometry_msgs/PoseStamped pose_img_2
geometry_msgs/PoseStamped pose_img_3

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['header','id','confidence','pose','pose_img_0','pose_img_1','pose_img_2','pose_img_3']
  _slot_types = ['std_msgs/Header','uint32','uint32','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,id,confidence,pose,pose_img_0,pose_img_1,pose_img_2,pose_img_3

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AlvarMarker, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.id is None:
        self.id = 0
      if self.confidence is None:
        self.confidence = 0
      if self.pose is None:
        self.pose = geometry_msgs.msg.PoseStamped()
      if self.pose_img_0 is None:
        self.pose_img_0 = geometry_msgs.msg.PoseStamped()
      if self.pose_img_1 is None:
        self.pose_img_1 = geometry_msgs.msg.PoseStamped()
      if self.pose_img_2 is None:
        self.pose_img_2 = geometry_msgs.msg.PoseStamped()
      if self.pose_img_3 is None:
        self.pose_img_3 = geometry_msgs.msg.PoseStamped()
    else:
      self.header = std_msgs.msg.Header()
      self.id = 0
      self.confidence = 0
      self.pose = geometry_msgs.msg.PoseStamped()
      self.pose_img_0 = geometry_msgs.msg.PoseStamped()
      self.pose_img_1 = geometry_msgs.msg.PoseStamped()
      self.pose_img_2 = geometry_msgs.msg.PoseStamped()
      self.pose_img_3 = geometry_msgs.msg.PoseStamped()

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_5I().pack(_x.id, _x.confidence, _x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs))
      _x = self.pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pose.pose.position.x, _x.pose.pose.position.y, _x.pose.pose.position.z, _x.pose.pose.orientation.x, _x.pose.pose.orientation.y, _x.pose.pose.orientation.z, _x.pose.pose.orientation.w, _x.pose_img_0.header.seq, _x.pose_img_0.header.stamp.secs, _x.pose_img_0.header.stamp.nsecs))
      _x = self.pose_img_0.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pose_img_0.pose.position.x, _x.pose_img_0.pose.position.y, _x.pose_img_0.pose.position.z, _x.pose_img_0.pose.orientation.x, _x.pose_img_0.pose.orientation.y, _x.pose_img_0.pose.orientation.z, _x.pose_img_0.pose.orientation.w, _x.pose_img_1.header.seq, _x.pose_img_1.header.stamp.secs, _x.pose_img_1.header.stamp.nsecs))
      _x = self.pose_img_1.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pose_img_1.pose.position.x, _x.pose_img_1.pose.position.y, _x.pose_img_1.pose.position.z, _x.pose_img_1.pose.orientation.x, _x.pose_img_1.pose.orientation.y, _x.pose_img_1.pose.orientation.z, _x.pose_img_1.pose.orientation.w, _x.pose_img_2.header.seq, _x.pose_img_2.header.stamp.secs, _x.pose_img_2.header.stamp.nsecs))
      _x = self.pose_img_2.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pose_img_2.pose.position.x, _x.pose_img_2.pose.position.y, _x.pose_img_2.pose.position.z, _x.pose_img_2.pose.orientation.x, _x.pose_img_2.pose.orientation.y, _x.pose_img_2.pose.orientation.z, _x.pose_img_2.pose.orientation.w, _x.pose_img_3.header.seq, _x.pose_img_3.header.stamp.secs, _x.pose_img_3.header.stamp.nsecs))
      _x = self.pose_img_3.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.pose_img_3.pose.position.x, _x.pose_img_3.pose.position.y, _x.pose_img_3.pose.position.z, _x.pose_img_3.pose.orientation.x, _x.pose_img_3.pose.orientation.y, _x.pose_img_3.pose.orientation.z, _x.pose_img_3.pose.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pose is None:
        self.pose = geometry_msgs.msg.PoseStamped()
      if self.pose_img_0 is None:
        self.pose_img_0 = geometry_msgs.msg.PoseStamped()
      if self.pose_img_1 is None:
        self.pose_img_1 = geometry_msgs.msg.PoseStamped()
      if self.pose_img_2 is None:
        self.pose_img_2 = geometry_msgs.msg.PoseStamped()
      if self.pose_img_3 is None:
        self.pose_img_3 = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 20
      (_x.id, _x.confidence, _x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs,) = _get_struct_5I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pose.pose.position.x, _x.pose.pose.position.y, _x.pose.pose.position.z, _x.pose.pose.orientation.x, _x.pose.pose.orientation.y, _x.pose.pose.orientation.z, _x.pose.pose.orientation.w, _x.pose_img_0.header.seq, _x.pose_img_0.header.stamp.secs, _x.pose_img_0.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose_img_0.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose_img_0.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pose_img_0.pose.position.x, _x.pose_img_0.pose.position.y, _x.pose_img_0.pose.position.z, _x.pose_img_0.pose.orientation.x, _x.pose_img_0.pose.orientation.y, _x.pose_img_0.pose.orientation.z, _x.pose_img_0.pose.orientation.w, _x.pose_img_1.header.seq, _x.pose_img_1.header.stamp.secs, _x.pose_img_1.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose_img_1.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose_img_1.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pose_img_1.pose.position.x, _x.pose_img_1.pose.position.y, _x.pose_img_1.pose.position.z, _x.pose_img_1.pose.orientation.x, _x.pose_img_1.pose.orientation.y, _x.pose_img_1.pose.orientation.z, _x.pose_img_1.pose.orientation.w, _x.pose_img_2.header.seq, _x.pose_img_2.header.stamp.secs, _x.pose_img_2.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose_img_2.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose_img_2.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pose_img_2.pose.position.x, _x.pose_img_2.pose.position.y, _x.pose_img_2.pose.position.z, _x.pose_img_2.pose.orientation.x, _x.pose_img_2.pose.orientation.y, _x.pose_img_2.pose.orientation.z, _x.pose_img_2.pose.orientation.w, _x.pose_img_3.header.seq, _x.pose_img_3.header.stamp.secs, _x.pose_img_3.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose_img_3.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose_img_3.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pose_img_3.pose.position.x, _x.pose_img_3.pose.position.y, _x.pose_img_3.pose.position.z, _x.pose_img_3.pose.orientation.x, _x.pose_img_3.pose.orientation.y, _x.pose_img_3.pose.orientation.z, _x.pose_img_3.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_5I().pack(_x.id, _x.confidence, _x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs))
      _x = self.pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pose.pose.position.x, _x.pose.pose.position.y, _x.pose.pose.position.z, _x.pose.pose.orientation.x, _x.pose.pose.orientation.y, _x.pose.pose.orientation.z, _x.pose.pose.orientation.w, _x.pose_img_0.header.seq, _x.pose_img_0.header.stamp.secs, _x.pose_img_0.header.stamp.nsecs))
      _x = self.pose_img_0.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pose_img_0.pose.position.x, _x.pose_img_0.pose.position.y, _x.pose_img_0.pose.position.z, _x.pose_img_0.pose.orientation.x, _x.pose_img_0.pose.orientation.y, _x.pose_img_0.pose.orientation.z, _x.pose_img_0.pose.orientation.w, _x.pose_img_1.header.seq, _x.pose_img_1.header.stamp.secs, _x.pose_img_1.header.stamp.nsecs))
      _x = self.pose_img_1.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pose_img_1.pose.position.x, _x.pose_img_1.pose.position.y, _x.pose_img_1.pose.position.z, _x.pose_img_1.pose.orientation.x, _x.pose_img_1.pose.orientation.y, _x.pose_img_1.pose.orientation.z, _x.pose_img_1.pose.orientation.w, _x.pose_img_2.header.seq, _x.pose_img_2.header.stamp.secs, _x.pose_img_2.header.stamp.nsecs))
      _x = self.pose_img_2.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pose_img_2.pose.position.x, _x.pose_img_2.pose.position.y, _x.pose_img_2.pose.position.z, _x.pose_img_2.pose.orientation.x, _x.pose_img_2.pose.orientation.y, _x.pose_img_2.pose.orientation.z, _x.pose_img_2.pose.orientation.w, _x.pose_img_3.header.seq, _x.pose_img_3.header.stamp.secs, _x.pose_img_3.header.stamp.nsecs))
      _x = self.pose_img_3.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.pose_img_3.pose.position.x, _x.pose_img_3.pose.position.y, _x.pose_img_3.pose.position.z, _x.pose_img_3.pose.orientation.x, _x.pose_img_3.pose.orientation.y, _x.pose_img_3.pose.orientation.z, _x.pose_img_3.pose.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pose is None:
        self.pose = geometry_msgs.msg.PoseStamped()
      if self.pose_img_0 is None:
        self.pose_img_0 = geometry_msgs.msg.PoseStamped()
      if self.pose_img_1 is None:
        self.pose_img_1 = geometry_msgs.msg.PoseStamped()
      if self.pose_img_2 is None:
        self.pose_img_2 = geometry_msgs.msg.PoseStamped()
      if self.pose_img_3 is None:
        self.pose_img_3 = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 20
      (_x.id, _x.confidence, _x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs,) = _get_struct_5I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pose.pose.position.x, _x.pose.pose.position.y, _x.pose.pose.position.z, _x.pose.pose.orientation.x, _x.pose.pose.orientation.y, _x.pose.pose.orientation.z, _x.pose.pose.orientation.w, _x.pose_img_0.header.seq, _x.pose_img_0.header.stamp.secs, _x.pose_img_0.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose_img_0.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose_img_0.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pose_img_0.pose.position.x, _x.pose_img_0.pose.position.y, _x.pose_img_0.pose.position.z, _x.pose_img_0.pose.orientation.x, _x.pose_img_0.pose.orientation.y, _x.pose_img_0.pose.orientation.z, _x.pose_img_0.pose.orientation.w, _x.pose_img_1.header.seq, _x.pose_img_1.header.stamp.secs, _x.pose_img_1.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose_img_1.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose_img_1.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pose_img_1.pose.position.x, _x.pose_img_1.pose.position.y, _x.pose_img_1.pose.position.z, _x.pose_img_1.pose.orientation.x, _x.pose_img_1.pose.orientation.y, _x.pose_img_1.pose.orientation.z, _x.pose_img_1.pose.orientation.w, _x.pose_img_2.header.seq, _x.pose_img_2.header.stamp.secs, _x.pose_img_2.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose_img_2.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose_img_2.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pose_img_2.pose.position.x, _x.pose_img_2.pose.position.y, _x.pose_img_2.pose.position.z, _x.pose_img_2.pose.orientation.x, _x.pose_img_2.pose.orientation.y, _x.pose_img_2.pose.orientation.z, _x.pose_img_2.pose.orientation.w, _x.pose_img_3.header.seq, _x.pose_img_3.header.stamp.secs, _x.pose_img_3.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose_img_3.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose_img_3.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pose_img_3.pose.position.x, _x.pose_img_3.pose.position.y, _x.pose_img_3.pose.position.z, _x.pose_img_3.pose.orientation.x, _x.pose_img_3.pose.orientation.y, _x.pose_img_3.pose.orientation.z, _x.pose_img_3.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7d3I = None
def _get_struct_7d3I():
    global _struct_7d3I
    if _struct_7d3I is None:
        _struct_7d3I = struct.Struct("<7d3I")
    return _struct_7d3I
_struct_5I = None
def _get_struct_5I():
    global _struct_5I
    if _struct_5I is None:
        _struct_5I = struct.Struct("<5I")
    return _struct_5I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
