from copy import deepcopy
import numpy as np

from mani_skill2_real2sim.agents.controllers import *
from mani_skill2_real2sim.sensors.camera import CameraConfig

class UnitreeG1DefaultConfig:
    def __init__(self) -> None:
        self.urdf_path = "{PACKAGE_ASSET_DIR}/descriptions/unitree_g1/unitree_g1.urdf"
        
        # URDF configurations (if any specific material or collision properties)
        self.urdf_config = dict(
            # Define materials or other properties if needed
        )
        
        # Joint names
        self.joint_names = ['left_hip_pitch_joint', 'right_hip_pitch_joint', 'waist_yaw_joint', 'left_hip_roll_joint', 'right_hip_roll_joint', 'waist_roll_joint', 'left_hip_yaw_joint', 'right_hip_yaw_joint', 'waist_pitch_joint', 'left_knee_joint', 'right_knee_joint', 'left_shoulder_pitch_joint', 'right_shoulder_pitch_joint', 'left_ankle_pitch_joint', 'right_ankle_pitch_joint', 'left_shoulder_roll_joint', 'right_shoulder_roll_joint', 'left_ankle_roll_joint', 'right_ankle_roll_joint', 'left_shoulder_yaw_joint', 'right_shoulder_yaw_joint', 'left_elbow_joint', 'right_elbow_joint', 'left_wrist_roll_joint', 'right_wrist_roll_joint', 'left_wrist_pitch_joint', 'right_wrist_pitch_joint', 'left_wrist_yaw_joint', 'right_wrist_yaw_joint'] 
        
        # Controller parameters
        self.stiffness = 50.0  # Placeholder values
        self.damping = 1.0     # Placeholder values
        self.force_limit = 100
        
        # End-effector link name (if applicable)
        self.ee_link_name = "base_link"  # Replace with appropriate link name
        
    @property
    def controllers(self):
        # Define controller configurations
        joint_position_controller = PDJointPosControllerConfig(
            joint_names=self.joint_names,
            lower_limits=-np.pi,
            upper_limits=np.pi,
            stiffness=self.stiffness,
            damping=self.damping,
            force_limit=self.force_limit,
            normalize_action=True,  # Adjust based on your needs
        )
        
        # Return a dictionary of controllers
        controller_configs = dict(
            joint_position=joint_position_controller,
            # Add other controllers if needed
        )
        
        return deepcopy(controller_configs)
        
    @property
    def cameras(self):
        # Define camera configurations if the robot has cameras
        return CameraConfig(
            uid="front_camera",
            p=[0.1, 0.0, 0.2],  # Replace with actual position
            q=[1, 0, 0, 0],     # Replace with actual orientation
            width=640,
            height=480,
            fx=500.0,  # Replace with calibrated values
            fy=500.0,
            cx=320.0,
            cy=240.0,
            actor_uid="head_link",  # Replace with actual link name
        )
