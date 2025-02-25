// Generated by gencpp from file ca_msgs/PlaySong.msg
// DO NOT EDIT!


#ifndef CA_MSGS_MESSAGE_PLAYSONG_H
#define CA_MSGS_MESSAGE_PLAYSONG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ca_msgs
{
template <class ContainerAllocator>
struct PlaySong_
{
  typedef PlaySong_<ContainerAllocator> Type;

  PlaySong_()
    : song(0)  {
    }
  PlaySong_(const ContainerAllocator& _alloc)
    : song(0)  {
  (void)_alloc;
    }



   typedef uint8_t _song_type;
  _song_type song;





  typedef boost::shared_ptr< ::ca_msgs::PlaySong_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ca_msgs::PlaySong_<ContainerAllocator> const> ConstPtr;

}; // struct PlaySong_

typedef ::ca_msgs::PlaySong_<std::allocator<void> > PlaySong;

typedef boost::shared_ptr< ::ca_msgs::PlaySong > PlaySongPtr;
typedef boost::shared_ptr< ::ca_msgs::PlaySong const> PlaySongConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ca_msgs::PlaySong_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ca_msgs::PlaySong_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ca_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'HasHeader': False, 'IsMessage': True, 'IsFixedSize': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'ca_msgs': ['/home/developer/low_cost_ws/src/pyrobot/robots/LoCoBot/thirdparty/create_autonomy/ca_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct HasHeader< ::ca_msgs::PlaySong_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ca_msgs::PlaySong_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ca_msgs::PlaySong_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ca_msgs::PlaySong_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ca_msgs::PlaySong_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ca_msgs::PlaySong_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ca_msgs::PlaySong_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eb55a5c354f06b6572d1ec46a28b6e6a";
  }

  static const char* value(const ::ca_msgs::PlaySong_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeb55a5c354f06b65ULL;
  static const uint64_t static_value2 = 0x72d1ec46a28b6e6aULL;
};

template<class ContainerAllocator>
struct DataType< ::ca_msgs::PlaySong_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ca_msgs/PlaySong";
  }

  static const char* value(const ::ca_msgs::PlaySong_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ca_msgs::PlaySong_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 song      # song number [0-3]\n\
";
  }

  static const char* value(const ::ca_msgs::PlaySong_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ca_msgs::PlaySong_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.song);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PlaySong_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ca_msgs::PlaySong_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ca_msgs::PlaySong_<ContainerAllocator>& v)
  {
    s << indent << "song: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.song);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CA_MSGS_MESSAGE_PLAYSONG_H
