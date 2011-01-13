

manufacturers = [
  {'id': 161,
   'name': u'Creative Lighting',
   'pids': [
      {'get_request': {'is_repeated': False, 'items': []},
       'get_response': {'is_repeated': False,
                        'items': [{'name': u'mode', 'type': 'uint8'}]},
       'get_sub_device_range': 2,
       'name': u'DEVICE_MODE',
       'set_request': {'is_repeated': False,
                       'items': [{'name': u'mode', 'type': 'uint8'}]},
       'set_response': {'is_repeated': False, 'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.creativelighting.com.au/datasheets/RDM%20Supplement.pdf',
       'notes': 'Controls the operating mode of the device<br><ul><li>0: DMX512</li><li>1: DALI</li><li>2: DSI</li></ul>',
       'value': 32768}]
  },
  {'id': 21324,
   'pids': [
      {'get_request': {'is_repeated': False, 'items': []},
       'get_response': {'is_repeated': False,
                        'items': [{'name': u'mode', 'type': 'uint8'}]},
       'get_sub_device_range': 2,
       'name': u'DMX_HOLD_MODE',
       'set_request': {'is_repeated': False,
                       'items': [{'name': u'mode', 'type': 'uint8'}]},
       'set_response': {'is_repeated': False, 'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
       'notes': 'Controls the behavior of the device when the signal fails.<br><ul><li>0: No hold, outputs go to 0</li><li>1: No hold, outputs go to 100%</li><li>2: Hold last DMX</li><li>3: No hold, go to predefined scene.</li></ul>',
       'value': 33009},
      {'get_request': {'is_repeated': False, 'items': []},
       'get_response': {'is_repeated': False,
                        'items': [{'name': u'scale_value', 'type': 'uint8'}]},
       'get_sub_device_range': 2,
       'name': u'DC_CALIBRATION',
       'set_request': {'is_repeated': False,
                       'items': [{'name': u'scale_value', 'type': 'uint8'}]},
       'set_response': {'is_repeated': False, 'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
       'notes': 'With the parameters, the outputs can be scaled to the desired maximum valu',
       'value': 56522},
      {'get_request': {'is_repeated': False, 'items': []},
       'get_response': {'is_repeated': True,
                        'items': [{'name': u'offset_value', 'type': 'uint8'}]},
       'get_sub_device_range': 2,
       'name': u'DC_OFFSET',
       'set_request': {'is_repeated': True,
                       'items': [{'name': u'offset_value', 'type': 'uint8'}]},
       'set_response': {'is_repeated': False, 'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
       'notes': 'With the parameters, the offset adjustment of the outputs are set to the desired value. It is transmitted as many values as outputs must be set. The number is determined by the parameters length (PDL).  The offset input is especially useful when driving LEDs with a different starting point',
       'value': 56334},
      {'name': u'DC_FADER_OFFSET',
       'set_request': {'is_repeated': False,
                       'items': [{'name': u'offset_value', 'type': 'uint8'}]},
       'set_response': {'is_repeated': False, 'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
       'notes': 'With the parameters, the offset adjustment of the outputs are set to the desired value. The values are collected directly from the DMX input (the last valid zero weather package). There are are as many values as outputs must be set. The acquisition is initiated by the command. A reading is possible with the function DC_OFFSET. ',
       'value': 56335},
#      {'get_request': {'is_repeated': False, 'items': []},
#       'get_response': {'is_repeated': True,
#                        'items': [{'name': u'offset_value', 'type': 'uint8'}]},
#       'get_sub_device_range': 2,
#       'name': u'dc_offset',
#       'set_request': {'is_repeated': True,
#                       'items': [{'name': u'offset_value', 'type': 'uint8'}]},
#       'set_response': {'is_repeated': False, 'items': []},
#       'set_sub_device_range': 1,
#       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
#       'notes': 'With the parameter, the output characteristic can be adjusted.  It will, the curve number, the number of available curves, the number of nodes, the interpolation method, and subsequently transferred n +1 nodes. For a graph with 8 linear segments, for example: $ 01, $ 01, $ 08, $ 01, $ 00, $ 1F, $ 3F, $ 5F, $ 7F, $ 9F, $ BF, $ DF, $ FF',
#       'value': 56525},
     ]
   },
]


pids = [{'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'label',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'DEVICE_MODEL_DESCRIPTION',
  'value': 128},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'label',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'MANUFACTURER_LABEL',
  'value': 129},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'label',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'DEVICE_LABEL',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'label',
                             'size': 32,
                             'type': 'string'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 130},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'state', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'LAMP_STATE',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'state', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1027},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'mode', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'LAMP_ON_MODE',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'mode', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1028},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'power_cycles', 'type': 'uint32'}]},
  'get_sub_device_range': 2,
  'name': u'DEVICE_POWER_CYCLES',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'power_cycles', 'type': 'uint32'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1029},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'identify_state', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'IDENTIFY_DEVICE',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'identify_state', 'type': 'bool'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 4096},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'version', 'type': 'uint32'}]},
  'get_sub_device_range': 2,
  'name': u'BOOT_SOFTWARE_VERSION',
  'value': 193},
 {'name': u'record_sensors',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'sensor_number', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 514},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': True,
                   'items': [{'name': u'manufacturer_id', 'type': 'uint16'},
                             {'name': u'device_id', 'type': 'uint32'}]},
  'get_sub_device_range': 0,
  'name': u'PROXIED_DEVICES',
  'value': 16},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'device_count', 'type': 'uint16'},
                             {'name': u'list_changed', 'type': 'bool'}]},
  'get_sub_device_range': 0,
  'name': u'PROXIED_DEVICE_COUNT',
  'value': 17},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'year', 'type': 'uint16'},
                             {'name': u'month', 'type': 'uint8'},
                             {'name': u'day', 'type': 'uint8'},
                             {'name': u'hour', 'type': 'uint8'},
                             {'name': u'minute', 'type': 'uint8'},
                             {'name': u'second', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'REAL_TIME_CLOCK',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'year', 'type': 'uint16'},
                            {'name': u'month', 'type': 'uint8'},
                            {'name': u'day', 'type': 'uint8'},
                            {'name': u'hour', 'type': 'uint8'},
                            {'name': u'minute', 'type': 'uint8'},
                            {'name': u'second', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1539},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'short_message', 'type': 'uint16'},
                             {'name': u'length_mismatch', 'type': 'uint16'},
                             {'name': u'checksum_fail', 'type': 'uint16'}]},
  'get_sub_device_range': 0,
  'name': u'COMMS_STATUS',
  'set_request': {'is_repeated': False, 'items': []},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 0,
  'value': 21},
 {'get_request': {'is_repeated': False,
                  'items': [{'name': u'sensor_number', 'type': 'uint8'}]},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'sensor_number', 'type': 'uint8'},
                             {'name': u'type', 'type': 'uint8'},
                             {'name': u'unit', 'type': 'uint8'},
                             {'name': u'prefix', 'type': 'uint8'},
                             {'name': u'range_min', 'type': 'uint16'},
                             {'name': u'range_max', 'type': 'uint16'},
                             {'name': u'normal_min', 'type': 'uint16'},
                             {'name': u'normal_max', 'type': 'uint16'},
                             {'name': u'supports_recording',
                              'type': 'uint8'},
                             {'name': u'name',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'SENSOR_DEFINITION',
  'value': 512},
 {'get_request': {'is_repeated': False,
                  'items': [{'name': u'status_type', 'type': 'uint8'}]},
  'get_response': {'is_repeated': False, 'items': []},
  'get_sub_device_range': 0,
  'name': u'QUEUED_MESSAGE',
  'value': 32},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'language',
                              'size': 2,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'LANGUAGE',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'language',
                             'size': 2,
                             'type': 'string'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 176},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': True,
                   'items': [{'name': u'slot_offset', 'type': 'uint16'},
                             {'name': u'default_slot_value',
                              'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'DEFAULT_SLOT_VALUE',
  'value': 290},
 {'name': u'reset_device',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'reset_mode', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 4097},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'hours', 'type': 'uint32'}]},
  'get_sub_device_range': 2,
  'name': u'DEVICE_HOURS',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'hours', 'type': 'uint32'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1024},
 {'name': u'CAPTURE_PRESET',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'scene', 'type': 'uint16'},
                            {'name': u'fade_up_time', 'type': 'uint16'},
                            {'name': u'fade_down_time', 'type': 'uint16'},
                            {'name': u'wait_time', 'type': 'uint16'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 4144},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'dmx_address', 'type': 'uint16'}]},
  'get_sub_device_range': 2,
  'name': u'DMX_START_ADDRESS',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'dmx_address', 'type': 'uint16'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 240},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'invert_status', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'DISPLAY_INVERT',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'invert_status', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1280},
 {'get_request': {'is_repeated': False,
                  'items': [{'name': u'status_type', 'type': 'uint8'}]},
  'get_response': {'is_repeated': True,
                   'items': [{'name': u'sub_device', 'type': 'uint16'},
                             {'name': u'status_type', 'type': 'uint8'},
                             {'name': u'message_id', 'type': 'uint16'},
                             {'name': u'value1', 'type': 'uint16'},
                             {'name': u'value2', 'type': 'uint16'}]},
  'get_sub_device_range': 0,
  'name': u'STATUS_MESSAGE',
  'value': 48},
 {'get_request': {'is_repeated': False,
                  'items': [{'name': u'status_id', 'type': 'uint16'}]},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'label',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 0,
  'name': u'STATUS_ID_DESCRIPTION',
  'value': 49},
 {'name': u'CLEAR_STATUS_ID',
  'set_request': {'is_repeated': False, 'items': []},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 50},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'status_type', 'type': 'uint8'}]},
  'get_sub_device_range': 3,
  'name': u'SUB_DEVICE_STATUS_REPORT_THRESHOLD',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'status_type', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 51},
 {'get_request': {'is_repeated': False,
                  'items': [{'name': u'sensor_number', 'type': 'uint8'}]},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'sensor_number', 'type': 'uint8'},
                             {'name': u'present_value', 'type': 'uint16'},
                             {'name': u'lowest', 'type': 'uint16'},
                             {'name': u'highest', 'type': 'uint16'},
                             {'name': u'recorded', 'type': 'uint16'}]},
  'get_sub_device_range': 2,
  'name': u'SENSOR_VALUE',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'sensor_number', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False,
                   'items': [{'name': u'sensor_number', 'type': 'uint8'},
                             {'name': u'present_value', 'type': 'uint16'},
                             {'name': u'lowest', 'type': 'uint16'},
                             {'name': u'highest', 'type': 'uint16'},
                             {'name': u'recorded', 'type': 'uint16'}]},
  'set_sub_device_range': 1,
  'value': 513},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'invert', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'PAN_INVERT',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'invert', 'type': 'bool'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1536},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'label',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'SOFTWARE_VERSION_LABEL',
  'value': 192},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': True,
                   'items': [{'name': u'language',
                              'size': 2,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'LANGUAGE_CAPABILITIES',
  'value': 160},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'label',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'BOOT_SOFTWARE_LABEL',
  'value': 194},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'hours', 'type': 'uint32'}]},
  'get_sub_device_range': 2,
  'name': u'LAMP_HOURS',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'hours', 'type': 'uint32'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1025},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'mode', 'type': 'uint16'},
                             {'name': u'level', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'PRESET_PLAYBACK',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'mode', 'type': 'uint16'},
                            {'name': u'level', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 4145},
 {'get_request': {'is_repeated': False,
                  'items': [{'name': u'personality', 'type': 'uint8'}]},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'personality', 'type': 'uint8'},
                             {'name': u'slots_required', 'type': 'uint16'},
                             {'name': u'name',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'DMX_PERSONALITY_DESCRIPTION',
  'value': 225},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'level', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'DISPLAY_LEVEL',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'level', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1281},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'current_personality',
                              'type': 'uint8'},
                             {'name': u'personality_count',
                              'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'DMX_PERSONALITY',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'personality', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 224},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': True,
                   'items': [{'name': u'slot_offset', 'type': 'uint16'},
                             {'name': u'slot_type', 'type': 'uint8'},
                             {'name': u'slot_label_id', 'type': 'uint16'}]},
  'get_sub_device_range': 2,
  'name': u'SLOT_INFO',
  'value': 288},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': True,
                   'items': [{'name': u'param', 'type': 'uint16'}]},
  'get_sub_device_range': 2,
  'name': u'SUPPORTED_PARAMETERS',
  'value': 80},
 {'get_request': {'is_repeated': False,
                  'items': [{'name': u'pid', 'type': 'uint16'}]},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'pid', 'type': 'uint16'},
                             {'name': u'pdl_size', 'type': 'uint8'},
                             {'name': u'data_type', 'type': 'uint8'},
                             {'name': u'command_class', 'type': 'uint8'},
                             {'name': u'type', 'type': 'uint8'},
                             {'name': u'unit', 'type': 'uint8'},
                             {'name': u'prefix', 'type': 'uint8'},
                             {'name': u'min_value', 'type': 'uint32'},
                             {'name': u'max_value', 'type': 'uint32'},
                             {'name': u'default_value', 'type': 'uint32'},
                             {'name': u'description',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 0,
  'name': u'PARAMETER_DESCRIPTION',
  'value': 81},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'invert', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'TILT_INVERT',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'invert', 'type': 'bool'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1537},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'protocol_major', 'type': 'uint8'},
                             {'name': u'protocol_minor', 'type': 'uint8'},
                             {'name': u'device_model', 'type': 'uint16'},
                             {'name': u'product_category',
                              'type': 'uint16'},
                             {'name': u'software_version',
                              'type': 'uint32'},
                             {'name': u'dmx_footprint', 'type': 'uint16'},
                             {'name': u'current_personality',
                              'type': 'uint8'},
                             {'name': u'personality_count',
                              'type': 'uint8'},
                             {'name': u'start_address', 'type': 'uint16'},
                             {'name': u'sub_device_count',
                              'type': 'uint16'},
                             {'name': u'sensor_count', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'DEVICE_INFO',
  'value': 96},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'using_defaults', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'FACTORY_DEFAULTS',
  'set_request': {'is_repeated': False, 'items': []},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 144},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'strikes', 'type': 'uint32'}]},
  'get_sub_device_range': 2,
  'name': u'LAMP_STRIKES',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'strikes', 'type': 'uint32'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1026},
 {'get_request': {'is_repeated': False,
                  'items': [{'name': u'test_number', 'type': 'uint8'}]},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'test_number', 'type': 'uint8'},
                             {'name': u'description',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'SELF_TEST_DESCRIPTION',
  'value': 4129},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'state', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'POWER_STATE',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'state', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 4112},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'tests_active', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'PERFORM_SELF_TEST',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'test_number', 'type': 'uint8'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 4128},
 {'get_request': {'is_repeated': False,
                  'items': [{'name': u'slot_number', 'type': 'uint16'}]},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'slot_number', 'type': 'uint16'},
                             {'name': u'name',
                              'size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'SLOT_DESCRIPTION',
  'value': 289},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': True,
                   'items': [{'name': u'detail_id', 'type': 'uint16'}],
                   'max_repeats': 6},
  'get_sub_device_range': 2,
  'name': u'PRODUCT_DETAIL_ID_LIST',
  'value': 112},
 {'get_request': {'is_repeated': False, 'items': []},
  'get_response': {'is_repeated': False,
                   'items': [{'name': u'swap', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'PAN_TILT_SWAP',
  'set_request': {'is_repeated': False,
                  'items': [{'name': u'swap', 'type': 'bool'}]},
  'set_response': {'is_repeated': False, 'items': []},
  'set_sub_device_range': 1,
  'value': 1538}]
