// Auto-generated. Do not edit!

// (in-package interbotix_sdk.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class OperatingModesRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.cmd = null;
      this.mode = null;
      this.joint_name = null;
      this.use_custom_profiles = null;
      this.profile_velocity = null;
      this.profile_acceleration = null;
    }
    else {
      if (initObj.hasOwnProperty('cmd')) {
        this.cmd = initObj.cmd
      }
      else {
        this.cmd = 0;
      }
      if (initObj.hasOwnProperty('mode')) {
        this.mode = initObj.mode
      }
      else {
        this.mode = '';
      }
      if (initObj.hasOwnProperty('joint_name')) {
        this.joint_name = initObj.joint_name
      }
      else {
        this.joint_name = '';
      }
      if (initObj.hasOwnProperty('use_custom_profiles')) {
        this.use_custom_profiles = initObj.use_custom_profiles
      }
      else {
        this.use_custom_profiles = false;
      }
      if (initObj.hasOwnProperty('profile_velocity')) {
        this.profile_velocity = initObj.profile_velocity
      }
      else {
        this.profile_velocity = 0;
      }
      if (initObj.hasOwnProperty('profile_acceleration')) {
        this.profile_acceleration = initObj.profile_acceleration
      }
      else {
        this.profile_acceleration = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OperatingModesRequest
    // Serialize message field [cmd]
    bufferOffset = _serializer.int8(obj.cmd, buffer, bufferOffset);
    // Serialize message field [mode]
    bufferOffset = _serializer.string(obj.mode, buffer, bufferOffset);
    // Serialize message field [joint_name]
    bufferOffset = _serializer.string(obj.joint_name, buffer, bufferOffset);
    // Serialize message field [use_custom_profiles]
    bufferOffset = _serializer.bool(obj.use_custom_profiles, buffer, bufferOffset);
    // Serialize message field [profile_velocity]
    bufferOffset = _serializer.int32(obj.profile_velocity, buffer, bufferOffset);
    // Serialize message field [profile_acceleration]
    bufferOffset = _serializer.int32(obj.profile_acceleration, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OperatingModesRequest
    let len;
    let data = new OperatingModesRequest(null);
    // Deserialize message field [cmd]
    data.cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [mode]
    data.mode = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [joint_name]
    data.joint_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [use_custom_profiles]
    data.use_custom_profiles = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [profile_velocity]
    data.profile_velocity = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [profile_acceleration]
    data.profile_acceleration = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.mode);
    length += _getByteLength(object.joint_name);
    return length + 18;
  }

  static datatype() {
    // Returns string type for a service object
    return 'interbotix_sdk/OperatingModesRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '585951edcc6006e2034f68a456aad669';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Set the operating modes for the arm, gripper, or a single joint
    #
    # There are four options when setting operating modes:
    #   1) ARM_JOINTS_AND_GRIPPER - affects the operating modes for all joints, including the gripper.
    #   2) ARM_JOINTS - affects the operating modes for all joints, excluding the gripper.
    #   3) GRIPPER - affects the operating mode only for the gripper
    #   4) SINGLE_JOINT - affects the operating mode for the joint specified by 'joint_name'.
    #                     Note that the 'joint_name' parameter only needs to be used for this
    #                     option. For any other option, it can be left blank.
    # Set the option to the 'cmd' parameter and the 'joint_name' to the specified joint (if doing the
    # SINGLE_JOINT option).
    
    # There are 5 valid operating modes for the arm. They are...
    #   "none" - arm motors will not respond to any joint command
    #   "position" - arm motors will expect only position commands
    #   "velocity" - arm motors will expect only velocity commands
    #   "current" - arm motors will expect only current commands
    #   "pwm" - arm motors will expect only pwm commands
    #
    # The gripper can also be set to "ext_position". This allows the gripper to do
    # multiple rotations instead of just one. It should only be used if you are using
    # a custom gripper capable of doing more than one rotation.
    #
    # For "position" control, profile_velocity sets the max speed of each joint while
    # profile_acceleration sets the max acceleration. Please reference the motor datasheet
    # (just click a motor at http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/)
    # for conversion factors. Values can be between 0 and 32,767. If setting custom profiles,
    # make sure to set 'use_custom_x_profiles' to true.
    #
    # For "velocity" control, only profile_acceleration is used.
    #
    # The velocity and acceleration profiles are not used in the "current" and "pwm" modes.
    
    int8 ARM_JOINTS_AND_GRIPPER = 1
    int8 ARM_JOINTS = 2
    int8 GRIPPER = 3
    int8 SINGLE_JOINT = 4
    
    int8 cmd
    string mode
    string joint_name
    bool use_custom_profiles
    int32 profile_velocity
    int32 profile_acceleration
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new OperatingModesRequest(null);
    if (msg.cmd !== undefined) {
      resolved.cmd = msg.cmd;
    }
    else {
      resolved.cmd = 0
    }

    if (msg.mode !== undefined) {
      resolved.mode = msg.mode;
    }
    else {
      resolved.mode = ''
    }

    if (msg.joint_name !== undefined) {
      resolved.joint_name = msg.joint_name;
    }
    else {
      resolved.joint_name = ''
    }

    if (msg.use_custom_profiles !== undefined) {
      resolved.use_custom_profiles = msg.use_custom_profiles;
    }
    else {
      resolved.use_custom_profiles = false
    }

    if (msg.profile_velocity !== undefined) {
      resolved.profile_velocity = msg.profile_velocity;
    }
    else {
      resolved.profile_velocity = 0
    }

    if (msg.profile_acceleration !== undefined) {
      resolved.profile_acceleration = msg.profile_acceleration;
    }
    else {
      resolved.profile_acceleration = 0
    }

    return resolved;
    }
};

// Constants for message
OperatingModesRequest.Constants = {
  ARM_JOINTS_AND_GRIPPER: 1,
  ARM_JOINTS: 2,
  GRIPPER: 3,
  SINGLE_JOINT: 4,
}

class OperatingModesResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OperatingModesResponse
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OperatingModesResponse
    let len;
    let data = new OperatingModesResponse(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'interbotix_sdk/OperatingModesResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new OperatingModesResponse(null);
    return resolved;
    }
};

module.exports = {
  Request: OperatingModesRequest,
  Response: OperatingModesResponse,
  md5sum() { return '585951edcc6006e2034f68a456aad669'; },
  datatype() { return 'interbotix_sdk/OperatingModes'; }
};
