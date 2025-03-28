// Generated by gencpp from file interbotix_sdk/JointCommands.msg
// DO NOT EDIT!


#ifndef INTERBOTIX_SDK_MESSAGE_JOINTCOMMANDS_H
#define INTERBOTIX_SDK_MESSAGE_JOINTCOMMANDS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace interbotix_sdk
{
template <class ContainerAllocator>
struct JointCommands_
{
  typedef JointCommands_<ContainerAllocator> Type;

  JointCommands_()
    : cmd()  {
    }
  JointCommands_(const ContainerAllocator& _alloc)
    : cmd(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> _cmd_type;
  _cmd_type cmd;





  typedef boost::shared_ptr< ::interbotix_sdk::JointCommands_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::interbotix_sdk::JointCommands_<ContainerAllocator> const> ConstPtr;

}; // struct JointCommands_

typedef ::interbotix_sdk::JointCommands_<std::allocator<void> > JointCommands;

typedef boost::shared_ptr< ::interbotix_sdk::JointCommands > JointCommandsPtr;
typedef boost::shared_ptr< ::interbotix_sdk::JointCommands const> JointCommandsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::interbotix_sdk::JointCommands_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::interbotix_sdk::JointCommands_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::interbotix_sdk::JointCommands_<ContainerAllocator1> & lhs, const ::interbotix_sdk::JointCommands_<ContainerAllocator2> & rhs)
{
  return lhs.cmd == rhs.cmd;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::interbotix_sdk::JointCommands_<ContainerAllocator1> & lhs, const ::interbotix_sdk::JointCommands_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace interbotix_sdk

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::interbotix_sdk::JointCommands_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::interbotix_sdk::JointCommands_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::interbotix_sdk::JointCommands_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::interbotix_sdk::JointCommands_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::interbotix_sdk::JointCommands_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::interbotix_sdk::JointCommands_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::interbotix_sdk::JointCommands_<ContainerAllocator> >
{
  static const char* value()
  {
    return "306931a8f4b928ea86b21d23c7e4f90e";
  }

  static const char* value(const ::interbotix_sdk::JointCommands_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x306931a8f4b928eaULL;
  static const uint64_t static_value2 = 0x86b21d23c7e4f90eULL;
};

template<class ContainerAllocator>
struct DataType< ::interbotix_sdk::JointCommands_<ContainerAllocator> >
{
  static const char* value()
  {
    return "interbotix_sdk/JointCommands";
  }

  static const char* value(const ::interbotix_sdk::JointCommands_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::interbotix_sdk::JointCommands_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Send a vector of position [rad], velocity [rad/s], current [mA], or pwm commands to a group of joints synchronously\n"
"# as defined in the 'order' sequence in the motor config files (excludes the 'gripper' joint if present)\n"
"#\n"
"# The order of the joints is the same as the order of the joint names as published in the joint states topic\n"
"\n"
"float64[] cmd\n"
;
  }

  static const char* value(const ::interbotix_sdk::JointCommands_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::interbotix_sdk::JointCommands_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.cmd);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct JointCommands_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::interbotix_sdk::JointCommands_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::interbotix_sdk::JointCommands_<ContainerAllocator>& v)
  {
    s << indent << "cmd[]" << std::endl;
    for (size_t i = 0; i < v.cmd.size(); ++i)
    {
      s << indent << "  cmd[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.cmd[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // INTERBOTIX_SDK_MESSAGE_JOINTCOMMANDS_H
