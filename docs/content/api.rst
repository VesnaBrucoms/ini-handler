API
===

Basic Use
---------

Ini Handler is designed to be simple and lightweight to use. First off you will
need to import the Ini class and create a new instance::

  from ini_handler.vbini import Ini

  ini_file = Ini()

The Ini class has two keyword arguments, with defaults, in its constructor::

  filename='settings'
  directory=None

The directory kwarg will be set to different values depending on your OS: My Documents
for Windows machines, and the home directory for Linux. To use, you can simply
do the following:

Create and modify settings::

  ini_file['NewSetting'] = 'A new setting'
  ini_file['Bool'] = True
  ini_file['Integer'] = 1993

Get settings::

  ini_file['NewSetting']

The Ini class defines the __iter__ magic methed, so you can very easily iterate
over the settings. For each loop a tuple is returned with the setting key in
index 0 and the value in index 1::

  ini_file['Setting1'] = 'Value 1'
  ini_file['Setting2'] = 'Value 2'
  for setting in ini_file:
    print(setting)

  ('Setting1', 'Value 1')
  ('Setting2', 'Value 2')

Delete settings::

  del ini_file['OldSetting']

Get the number of settings::

  len(ini_file)

To create the .ini file itself all you have to call is::

  ini_file.save()

To read the settings back in call::

  ini_file.load()

Sections
--------

Settings can also be grouped into different sections. This is as simple as creating
or modifying a setting by passing a tuple, list, or set with element one as the
section name and element two as the actual value::

  ini_file['SettingKey'] = ('Section', 'Value')
  ini_file['Another'] = ['Section2', True]
  ini_file['Final'] = {'New Section', 2000}

And that's it! The Ini class behaves exactly as it did without grouping your
settings into different sections. Though if you ever want to get a section for a
particular settings, call::

  ini_file.get_setting_section('SettingKey')

And if you want to set a section::

  ini_file.set_setting_section('SettingKey', 'SectionName')
