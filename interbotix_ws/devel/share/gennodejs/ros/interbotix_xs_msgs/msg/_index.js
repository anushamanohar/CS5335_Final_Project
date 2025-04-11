
"use strict";

let TurretJoy = require('./TurretJoy.js');
let ArmJoy = require('./ArmJoy.js');
let JointSingleCommand = require('./JointSingleCommand.js');
let JointTrajectoryCommand = require('./JointTrajectoryCommand.js');
let JointTemps = require('./JointTemps.js');
let JointGroupCommand = require('./JointGroupCommand.js');
let HexJoy = require('./HexJoy.js');
let LocobotJoy = require('./LocobotJoy.js');

module.exports = {
  TurretJoy: TurretJoy,
  ArmJoy: ArmJoy,
  JointSingleCommand: JointSingleCommand,
  JointTrajectoryCommand: JointTrajectoryCommand,
  JointTemps: JointTemps,
  JointGroupCommand: JointGroupCommand,
  HexJoy: HexJoy,
  LocobotJoy: LocobotJoy,
};
