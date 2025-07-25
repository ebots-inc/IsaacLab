"""Configuration for the Boson robotic cell.

This module defines the following configuration:

* :obj:`BOSON_CELL_CFG`: Boson cell including two arms and a 3-DOF stage.

Reference: https://github.com/ebots/ebots_planning
"""

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

##
# Configuration
##

BOSON_CELL_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/root/mind/workspace/ebots_mind/ai_pipeline_server/assets/boson_cell.usd",
        activate_contact_sensors=False,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
        ),
        collision_props=sim_utils.CollisionPropertiesCfg(collision_enabled=False),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "arm_a_joint_1_s": 0.0,
            "arm_a_joint_2_l": 0.0,
            "arm_a_joint_3_u": 0.0,
            "arm_a_joint_4_r": 0.0,
            "arm_a_joint_5_b": 0.0,
            "arm_a_joint_6_t": 0.0,
            "arm_b_joint_1_s": 0.0,
            "arm_b_joint_2_l": 0.0,
            "arm_b_joint_3_u": 0.0,
            "arm_b_joint_4_r": 0.0,
            "arm_b_joint_5_b": 0.0,
            "arm_b_joint_6_t": 0.0,
        },
    ),
    actuators={
        "arm_b": ImplicitActuatorCfg(
            joint_names_expr=["arm_b.*"],
            effort_limit_sim=None,
            velocity_limit_sim=None,
            stiffness=None,
            damping=None,
        ),
        "arm_a": ImplicitActuatorCfg(
            joint_names_expr=["arm_a.*"],
            effort_limit_sim=None,
            velocity_limit_sim=None,
            stiffness=None,
            damping=None,
        ),
    },
    soft_joint_pos_limit_factor=1.0,
)
"""Configuration for the Boson robotic cell."""
