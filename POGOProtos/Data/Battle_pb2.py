# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Data.Battle.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data import Player_pb2 as POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data_dot_Player__pb2.POGOProtos_dot_Enums__pb2
from POGOProtos import Data_pb2 as POGOProtos_dot_Data__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Data_dot_Player__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Inventory_dot_Item__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Inventory_dot_Item__pb2
from POGOProtos.Data import Gym_pb2 as POGOProtos_dot_Data_dot_Gym__pb2
POGOProtos_dot_Data__pb2 = POGOProtos_dot_Data_dot_Gym__pb2.POGOProtos_dot_Data__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data_dot_Gym__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Data_dot_Player__pb2 = POGOProtos_dot_Data_dot_Gym__pb2.POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data_dot_Gym__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Inventory_dot_Item__pb2 = POGOProtos_dot_Data_dot_Gym__pb2.POGOProtos_dot_Inventory_dot_Item__pb2
POGOProtos_dot_Data_dot_Player__pb2 = POGOProtos_dot_Data_dot_Gym__pb2.POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data_dot_Gym__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Map_dot_Fort__pb2 = POGOProtos_dot_Data_dot_Gym__pb2.POGOProtos_dot_Map_dot_Fort__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data_dot_Gym__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Inventory_dot_Item__pb2 = POGOProtos_dot_Data_dot_Gym__pb2.POGOProtos_dot_Inventory_dot_Item__pb2

from POGOProtos.Data.Player_pb2 import *
from POGOProtos.Data_pb2 import *
from POGOProtos.Data.Gym_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos.Data.Battle.proto',
  package='POGOProtos.Data.Battle',
  syntax='proto3',
  serialized_pb=_b('\n\x1cPOGOProtos.Data.Battle.proto\x12\x16POGOProtos.Data.Battle\x1a\x1cPOGOProtos.Data.Player.proto\x1a\x15POGOProtos.Data.proto\x1a\x19POGOProtos.Data.Gym.proto\"\x85\x04\n\x0c\x42\x61ttleAction\x12\x36\n\x04Type\x18\x01 \x01(\x0e\x32(.POGOProtos.Data.Battle.BattleActionType\x12\x17\n\x0f\x61\x63tion_start_ms\x18\x02 \x01(\x03\x12\x13\n\x0b\x64uration_ms\x18\x03 \x01(\x05\x12\x14\n\x0c\x65nergy_delta\x18\x05 \x01(\x05\x12\x16\n\x0e\x61ttacker_index\x18\x06 \x01(\x05\x12\x14\n\x0ctarget_index\x18\x07 \x01(\x05\x12\x19\n\x11\x61\x63tive_pokemon_id\x18\x08 \x01(\x04\x12@\n\rplayer_joined\x18\t \x01(\x0b\x32).POGOProtos.Data.Battle.BattleParticipant\x12=\n\x0e\x62\x61ttle_results\x18\n \x01(\x0b\x32%.POGOProtos.Data.Battle.BattleResults\x12*\n\"damage_windows_start_timestamp_mss\x18\x0b \x01(\x03\x12(\n damage_windows_end_timestamp_mss\x18\x0c \x01(\x03\x12>\n\x0bplayer_left\x18\r \x01(\x0b\x32).POGOProtos.Data.Battle.BattleParticipant\x12\x19\n\x11target_pokemon_id\x18\x0e \x01(\x04\"\x8d\x02\n\tBattleLog\x12\x32\n\x05state\x18\x01 \x01(\x0e\x32#.POGOProtos.Data.Battle.BattleState\x12\x37\n\x0b\x62\x61ttle_type\x18\x02 \x01(\x0e\x32\".POGOProtos.Data.Battle.BattleType\x12\x11\n\tserver_ms\x18\x03 \x01(\x03\x12<\n\x0e\x62\x61ttle_actions\x18\x04 \x03(\x0b\x32$.POGOProtos.Data.Battle.BattleAction\x12!\n\x19\x62\x61ttle_start_timestamp_ms\x18\x05 \x01(\x03\x12\x1f\n\x17\x62\x61ttle_end_timestamp_ms\x18\x06 \x01(\x03\"\xac\x02\n\x11\x42\x61ttleParticipant\x12\x41\n\x0e\x61\x63tive_pokemon\x18\x01 \x01(\x0b\x32).POGOProtos.Data.Battle.BattlePokemonInfo\x12K\n\x16trainer_public_profile\x18\x02 \x01(\x0b\x32+.POGOProtos.Data.Player.PlayerPublicProfile\x12\x42\n\x0freverse_pokemon\x18\x03 \x03(\x0b\x32).POGOProtos.Data.Battle.BattlePokemonInfo\x12\x43\n\x10\x64\x65\x66\x65\x61ted_pokemon\x18\x04 \x03(\x0b\x32).POGOProtos.Data.Battle.BattlePokemonInfo\"w\n\x11\x42\x61ttlePokemonInfo\x12\x32\n\x0cpokemon_data\x18\x01 \x01(\x0b\x32\x1c.POGOProtos.Data.PokemonData\x12\x16\n\x0e\x63urrent_health\x18\x02 \x01(\x05\x12\x16\n\x0e\x63urrent_energy\x18\x03 \x01(\x05\"\xde\x01\n\rBattleResults\x12\x30\n\tgym_state\x18\x01 \x01(\x0b\x32\x1d.POGOProtos.Data.Gym.GymState\x12<\n\tattackers\x18\x02 \x03(\x0b\x32).POGOProtos.Data.Battle.BattleParticipant\x12!\n\x19player_experience_awarded\x18\x03 \x03(\x05\x12 \n\x18next_defender_pokemon_id\x18\x04 \x01(\x03\x12\x18\n\x10gym_points_delta\x18\x05 \x01(\x05*\xfc\x01\n\x10\x42\x61ttleActionType\x12\x10\n\x0c\x41\x43TION_UNSET\x10\x00\x12\x11\n\rACTION_ATTACK\x10\x01\x12\x10\n\x0c\x41\x43TION_DODGE\x10\x02\x12\x19\n\x15\x41\x43TION_SPECIAL_ATTACK\x10\x03\x12\x17\n\x13\x41\x43TION_SWAP_POKEMON\x10\x04\x12\x10\n\x0c\x41\x43TION_FAINT\x10\x05\x12\x16\n\x12\x41\x43TION_PLAYER_JOIN\x10\x06\x12\x16\n\x12\x41\x43TION_PLAYER_QUIT\x10\x07\x12\x12\n\x0e\x41\x43TION_VICTORY\x10\x08\x12\x11\n\rACTION_DEFEAT\x10\t\x12\x14\n\x10\x41\x43TION_TIMED_OUT\x10\n*T\n\x0b\x42\x61ttleState\x12\x0f\n\x0bSTATE_UNSET\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0b\n\x07VICTORY\x10\x02\x12\x0c\n\x08\x44\x45\x46\x45\x41TED\x10\x03\x12\r\n\tTIMED_OUT\x10\x04*=\n\nBattleType\x12\x15\n\x11\x42\x41TTLE_TYPE_UNSET\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x0c\n\x08TRAINING\x10\x02P\x00P\x01P\x02\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_Player__pb2.DESCRIPTOR,POGOProtos_dot_Data__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Gym__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_BATTLEACTIONTYPE = _descriptor.EnumDescriptor(
  name='BattleActionType',
  full_name='POGOProtos.Data.Battle.BattleActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_ATTACK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_DODGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_SPECIAL_ATTACK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_SWAP_POKEMON', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_FAINT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_PLAYER_JOIN', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_PLAYER_QUIT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_VICTORY', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_DEFEAT', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_TIMED_OUT', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1578,
  serialized_end=1830,
)
_sym_db.RegisterEnumDescriptor(_BATTLEACTIONTYPE)

BattleActionType = enum_type_wrapper.EnumTypeWrapper(_BATTLEACTIONTYPE)
_BATTLESTATE = _descriptor.EnumDescriptor(
  name='BattleState',
  full_name='POGOProtos.Data.Battle.BattleState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VICTORY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFEATED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_OUT', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1832,
  serialized_end=1916,
)
_sym_db.RegisterEnumDescriptor(_BATTLESTATE)

BattleState = enum_type_wrapper.EnumTypeWrapper(_BATTLESTATE)
_BATTLETYPE = _descriptor.EnumDescriptor(
  name='BattleType',
  full_name='POGOProtos.Data.Battle.BattleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BATTLE_TYPE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAINING', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1918,
  serialized_end=1979,
)
_sym_db.RegisterEnumDescriptor(_BATTLETYPE)

BattleType = enum_type_wrapper.EnumTypeWrapper(_BATTLETYPE)
ACTION_UNSET = 0
ACTION_ATTACK = 1
ACTION_DODGE = 2
ACTION_SPECIAL_ATTACK = 3
ACTION_SWAP_POKEMON = 4
ACTION_FAINT = 5
ACTION_PLAYER_JOIN = 6
ACTION_PLAYER_QUIT = 7
ACTION_VICTORY = 8
ACTION_DEFEAT = 9
ACTION_TIMED_OUT = 10
STATE_UNSET = 0
ACTIVE = 1
VICTORY = 2
DEFEATED = 3
TIMED_OUT = 4
BATTLE_TYPE_UNSET = 0
NORMAL = 1
TRAINING = 2



_BATTLEACTION = _descriptor.Descriptor(
  name='BattleAction',
  full_name='POGOProtos.Data.Battle.BattleAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='POGOProtos.Data.Battle.BattleAction.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_start_ms', full_name='POGOProtos.Data.Battle.BattleAction.action_start_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration_ms', full_name='POGOProtos.Data.Battle.BattleAction.duration_ms', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='energy_delta', full_name='POGOProtos.Data.Battle.BattleAction.energy_delta', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attacker_index', full_name='POGOProtos.Data.Battle.BattleAction.attacker_index', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_index', full_name='POGOProtos.Data.Battle.BattleAction.target_index', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_pokemon_id', full_name='POGOProtos.Data.Battle.BattleAction.active_pokemon_id', index=6,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_joined', full_name='POGOProtos.Data.Battle.BattleAction.player_joined', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_results', full_name='POGOProtos.Data.Battle.BattleAction.battle_results', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage_windows_start_timestamp_mss', full_name='POGOProtos.Data.Battle.BattleAction.damage_windows_start_timestamp_mss', index=9,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage_windows_end_timestamp_mss', full_name='POGOProtos.Data.Battle.BattleAction.damage_windows_end_timestamp_mss', index=10,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_left', full_name='POGOProtos.Data.Battle.BattleAction.player_left', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_pokemon_id', full_name='POGOProtos.Data.Battle.BattleAction.target_pokemon_id', index=12,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=654,
)


_BATTLELOG = _descriptor.Descriptor(
  name='BattleLog',
  full_name='POGOProtos.Data.Battle.BattleLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='POGOProtos.Data.Battle.BattleLog.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_type', full_name='POGOProtos.Data.Battle.BattleLog.battle_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_ms', full_name='POGOProtos.Data.Battle.BattleLog.server_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_actions', full_name='POGOProtos.Data.Battle.BattleLog.battle_actions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_start_timestamp_ms', full_name='POGOProtos.Data.Battle.BattleLog.battle_start_timestamp_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_end_timestamp_ms', full_name='POGOProtos.Data.Battle.BattleLog.battle_end_timestamp_ms', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=657,
  serialized_end=926,
)


_BATTLEPARTICIPANT = _descriptor.Descriptor(
  name='BattleParticipant',
  full_name='POGOProtos.Data.Battle.BattleParticipant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_pokemon', full_name='POGOProtos.Data.Battle.BattleParticipant.active_pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer_public_profile', full_name='POGOProtos.Data.Battle.BattleParticipant.trainer_public_profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse_pokemon', full_name='POGOProtos.Data.Battle.BattleParticipant.reverse_pokemon', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defeated_pokemon', full_name='POGOProtos.Data.Battle.BattleParticipant.defeated_pokemon', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=929,
  serialized_end=1229,
)


_BATTLEPOKEMONINFO = _descriptor.Descriptor(
  name='BattlePokemonInfo',
  full_name='POGOProtos.Data.Battle.BattlePokemonInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='POGOProtos.Data.Battle.BattlePokemonInfo.pokemon_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_health', full_name='POGOProtos.Data.Battle.BattlePokemonInfo.current_health', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_energy', full_name='POGOProtos.Data.Battle.BattlePokemonInfo.current_energy', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1231,
  serialized_end=1350,
)


_BATTLERESULTS = _descriptor.Descriptor(
  name='BattleResults',
  full_name='POGOProtos.Data.Battle.BattleResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_state', full_name='POGOProtos.Data.Battle.BattleResults.gym_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attackers', full_name='POGOProtos.Data.Battle.BattleResults.attackers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_experience_awarded', full_name='POGOProtos.Data.Battle.BattleResults.player_experience_awarded', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_defender_pokemon_id', full_name='POGOProtos.Data.Battle.BattleResults.next_defender_pokemon_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_points_delta', full_name='POGOProtos.Data.Battle.BattleResults.gym_points_delta', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1353,
  serialized_end=1575,
)

_BATTLEACTION.fields_by_name['Type'].enum_type = _BATTLEACTIONTYPE
_BATTLEACTION.fields_by_name['player_joined'].message_type = _BATTLEPARTICIPANT
_BATTLEACTION.fields_by_name['battle_results'].message_type = _BATTLERESULTS
_BATTLEACTION.fields_by_name['player_left'].message_type = _BATTLEPARTICIPANT
_BATTLELOG.fields_by_name['state'].enum_type = _BATTLESTATE
_BATTLELOG.fields_by_name['battle_type'].enum_type = _BATTLETYPE
_BATTLELOG.fields_by_name['battle_actions'].message_type = _BATTLEACTION
_BATTLEPARTICIPANT.fields_by_name['active_pokemon'].message_type = _BATTLEPOKEMONINFO
_BATTLEPARTICIPANT.fields_by_name['trainer_public_profile'].message_type = POGOProtos_dot_Data_dot_Player__pb2._PLAYERPUBLICPROFILE
_BATTLEPARTICIPANT.fields_by_name['reverse_pokemon'].message_type = _BATTLEPOKEMONINFO
_BATTLEPARTICIPANT.fields_by_name['defeated_pokemon'].message_type = _BATTLEPOKEMONINFO
_BATTLEPOKEMONINFO.fields_by_name['pokemon_data'].message_type = POGOProtos_dot_Data__pb2._POKEMONDATA
_BATTLERESULTS.fields_by_name['gym_state'].message_type = POGOProtos_dot_Data_dot_Gym__pb2._GYMSTATE
_BATTLERESULTS.fields_by_name['attackers'].message_type = _BATTLEPARTICIPANT
DESCRIPTOR.message_types_by_name['BattleAction'] = _BATTLEACTION
DESCRIPTOR.message_types_by_name['BattleLog'] = _BATTLELOG
DESCRIPTOR.message_types_by_name['BattleParticipant'] = _BATTLEPARTICIPANT
DESCRIPTOR.message_types_by_name['BattlePokemonInfo'] = _BATTLEPOKEMONINFO
DESCRIPTOR.message_types_by_name['BattleResults'] = _BATTLERESULTS
DESCRIPTOR.enum_types_by_name['BattleActionType'] = _BATTLEACTIONTYPE
DESCRIPTOR.enum_types_by_name['BattleState'] = _BATTLESTATE
DESCRIPTOR.enum_types_by_name['BattleType'] = _BATTLETYPE

BattleAction = _reflection.GeneratedProtocolMessageType('BattleAction', (_message.Message,), dict(
  DESCRIPTOR = _BATTLEACTION,
  __module__ = 'POGOProtos.Data.Battle_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Battle.BattleAction)
  ))
_sym_db.RegisterMessage(BattleAction)

BattleLog = _reflection.GeneratedProtocolMessageType('BattleLog', (_message.Message,), dict(
  DESCRIPTOR = _BATTLELOG,
  __module__ = 'POGOProtos.Data.Battle_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Battle.BattleLog)
  ))
_sym_db.RegisterMessage(BattleLog)

BattleParticipant = _reflection.GeneratedProtocolMessageType('BattleParticipant', (_message.Message,), dict(
  DESCRIPTOR = _BATTLEPARTICIPANT,
  __module__ = 'POGOProtos.Data.Battle_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Battle.BattleParticipant)
  ))
_sym_db.RegisterMessage(BattleParticipant)

BattlePokemonInfo = _reflection.GeneratedProtocolMessageType('BattlePokemonInfo', (_message.Message,), dict(
  DESCRIPTOR = _BATTLEPOKEMONINFO,
  __module__ = 'POGOProtos.Data.Battle_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Battle.BattlePokemonInfo)
  ))
_sym_db.RegisterMessage(BattlePokemonInfo)

BattleResults = _reflection.GeneratedProtocolMessageType('BattleResults', (_message.Message,), dict(
  DESCRIPTOR = _BATTLERESULTS,
  __module__ = 'POGOProtos.Data.Battle_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Battle.BattleResults)
  ))
_sym_db.RegisterMessage(BattleResults)


# @@protoc_insertion_point(module_scope)