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

class RegisterValuesRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.cmd = null;
      this.motor_name = null;
      this.addr_name = null;
      this.value = null;
    }
    else {
      if (initObj.hasOwnProperty('cmd')) {
        this.cmd = initObj.cmd
      }
      else {
        this.cmd = 0;
      }
      if (initObj.hasOwnProperty('motor_name')) {
        this.motor_name = initObj.motor_name
      }
      else {
        this.motor_name = '';
      }
      if (initObj.hasOwnProperty('addr_name')) {
        this.addr_name = initObj.addr_name
      }
      else {
        this.addr_name = '';
      }
      if (initObj.hasOwnProperty('value')) {
        this.value = initObj.value
      }
      else {
        this.value = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RegisterValuesRequest
    // Serialize message field [cmd]
    bufferOffset = _serializer.int8(obj.cmd, buffer, bufferOffset);
    // Serialize message field [motor_name]
    bufferOffset = _serializer.string(obj.motor_name, buffer, bufferOffset);
    // Serialize message field [addr_name]
    bufferOffset = _serializer.string(obj.addr_name, buffer, bufferOffset);
    // Serialize message field [value]
    bufferOffset = _serializer.int32(obj.value, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RegisterValuesRequest
    let len;
    let data = new RegisterValuesRequest(null);
    // Deserialize message field [cmd]
    data.cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [motor_name]
    data.motor_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [addr_name]
    data.addr_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [value]
    data.value = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.motor_name);
    length += _getByteLength(object.addr_name);
    return length + 13;
  }

  static datatype() {
    // Returns string type for a service object
    return 'interbotix_sdk/RegisterValuesRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '725e8187efb86073bd6c7e5fa5bb725f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Set or get the register(s) value(s) from motor(s)
    #
    # To get familiar with the register values, go to...
    # http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/
    # ...click on a motor model, and scroll down to the 'Control Table of RAM Area' section.
    #
    # There are four options to set or get a register value:
    #   1) ARM_JOINTS_AND_GRIPPER - affects the register values for all arm joints, including the gripper.
    #   2) ARM_JOINTS - affects the register values for all arm joints, excluding the gripper.
    #   3) GRIPPER - affects the register value only for the gripper
    #   4) SINGLE_MOTOR - affects the register for the motor specified by 'motor_name'.
    #                     Note that the 'motor_name' parameter only needs to be used for this
    #                     option. For any other option, it can be left blank.
    #
    # Set the option to the 'cmd' parameter and the 'motor_name' to the specified motor (if doing the
    # SINGLE_MOTOR option)..
    #
    # Next, set the 'addr_name' parameter to the name of the register to be written to or read from.
    #
    # If setting the register(s) value, set the 'value' parameter to the desired value. This value will be
    # written to either one or many motors depending on the 'cmd' option selected. Note that if a joint is
    # controlled by two motors and the register is in the RAM area, both motors' registers will be updated
    # with the desired value. If the register is in the EEPROM area, it must be modified with another service call.
    # As an FYI, if modifying an EEPROM register, the servo must first be torqued off.
    #
    # If reading the register(s) values, do not set the 'value' parameter. Instead, call the service at this
    # stage. The 'values' vector will be automatically updated with the register(s) value(s). If reading from
    # multiple joints at a time, the indexes of the values correspond with the joint names at those indexes in the
    # joint_states.name vector.
    
    int8 ARM_JOINTS_AND_GRIPPER = 1
    int8 ARM_JOINTS = 2
    int8 GRIPPER = 3
    int8 SINGLE_MOTOR = 4
    
    int8 cmd
    string motor_name
    string addr_name
    int32 value
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RegisterValuesRequest(null);
    if (msg.cmd !== undefined) {
      resolved.cmd = msg.cmd;
    }
    else {
      resolved.cmd = 0
    }

    if (msg.motor_name !== undefined) {
      resolved.motor_name = msg.motor_name;
    }
    else {
      resolved.motor_name = ''
    }

    if (msg.addr_name !== undefined) {
      resolved.addr_name = msg.addr_name;
    }
    else {
      resolved.addr_name = ''
    }

    if (msg.value !== undefined) {
      resolved.value = msg.value;
    }
    else {
      resolved.value = 0
    }

    return resolved;
    }
};

// Constants for message
RegisterValuesRequest.Constants = {
  ARM_JOINTS_AND_GRIPPER: 1,
  ARM_JOINTS: 2,
  GRIPPER: 3,
  SINGLE_MOTOR: 4,
}

class RegisterValuesResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.values = null;
    }
    else {
      if (initObj.hasOwnProperty('values')) {
        this.values = initObj.values
      }
      else {
        this.values = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RegisterValuesResponse
    // Serialize message field [values]
    bufferOffset = _arraySerializer.int32(obj.values, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RegisterValuesResponse
    let len;
    let data = new RegisterValuesResponse(null);
    // Deserialize message field [values]
    data.values = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.values.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'interbotix_sdk/RegisterValuesResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5dd1053b3769329bd3895728a55810d3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[] values
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RegisterValuesResponse(null);
    if (msg.values !== undefined) {
      resolved.values = msg.values;
    }
    else {
      resolved.values = []
    }

    return resolved;
    }
};

module.exports = {
  Request: RegisterValuesRequest,
  Response: RegisterValuesResponse,
  md5sum() { return 'c4b094ee6f4751519e444f39591c55e1'; },
  datatype() { return 'interbotix_sdk/RegisterValues'; }
};
