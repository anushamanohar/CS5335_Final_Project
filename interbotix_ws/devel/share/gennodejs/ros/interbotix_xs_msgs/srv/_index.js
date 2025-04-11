
"use strict";

let MotorGains = require('./MotorGains.js')
let RegisterValues = require('./RegisterValues.js')
let Reboot = require('./Reboot.js')
let RobotInfo = require('./RobotInfo.js')
let OperatingModes = require('./OperatingModes.js')
let TorqueEnable = require('./TorqueEnable.js')

module.exports = {
  MotorGains: MotorGains,
  RegisterValues: RegisterValues,
  Reboot: Reboot,
  RobotInfo: RobotInfo,
  OperatingModes: OperatingModes,
  TorqueEnable: TorqueEnable,
};
