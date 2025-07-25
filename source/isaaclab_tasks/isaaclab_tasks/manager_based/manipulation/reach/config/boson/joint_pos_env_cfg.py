# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import math

from isaaclab.utils import configclass

import isaaclab_tasks.manager_based.manipulation.reach.mdp as mdp
from isaaclab_tasks.manager_based.manipulation.reach.reach_env_cfg import ReachEnvCfg

##
# Pre-defined configs
##
from isaaclab_assets import BOSON_CELL_CFG  # isort: skip


##
# Environment configuration
##


@configclass
class BosonReachEnvCfg(ReachEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        # switch robot to boson
        self.scene.robot = BOSON_CELL_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
        # override rewards
        self.rewards.end_effector_position_tracking.params["asset_cfg"].body_names = ["arm_b_link_6_t"]
        self.rewards.end_effector_position_tracking_fine_grained.params["asset_cfg"].body_names = ["arm_b_link_6_t"]
        self.rewards.end_effector_orientation_tracking.params["asset_cfg"].body_names = ["arm_b_link_6_t"]

        # override actions
        self.actions.arm_action = mdp.JointPositionActionCfg(
            asset_name="robot", joint_names=["arm_b.*"], scale=0.5, use_default_offset=True
        )
        # override command generator body
        # end-effector is along z-direction
        self.commands.ee_pose.body_name = "arm_b_link_6_t"
        self.commands.ee_pose.ranges.pitch = (math.pi, math.pi)

