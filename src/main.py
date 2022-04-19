import dearpygui.dearpygui as dpg

dpg.create_context()

# 添加组
with dpg.window(label='Create Group', width=550, show=True):
    dpg.add_text(default_value='Create Group')
    dpg.add_input_text(label='Group Name')
    dpg.add_button(label='Submit')

# 删除组
with dpg.window(label='Delete Group', width=550, show=True):
    dpg.add_text(default_value='Select your group and delete', indent=10)
    dpg.add_combo(label='Group Name', indent=10, items=['Group A', 'Group B'], tag='api_group',
                  default_value='default')
    dpg.add_button(label='Submit', indent=10)

# 添加币安 api
with dpg.window(label='Create api', show=True, pos=[50, 100], width=550):
    dpg.add_text('Please enter your binance api bellow: ', indent=10)
    dpg.add_combo(label='Group Name', indent=10, items=[],
                  default_value='default')
    dpg.add_input_text(label='API Name', indent=10, )
    dpg.add_input_text(label='Key', indent=10, )
    dpg.add_input_text(label='Secret', indent=10, password=True)
    dpg.add_button(label='submit', indent=10)

# 删除币安 api
with dpg.window(label='delete api', pos=[60, 180], width=550):
    dpg.add_text('Please choose a api you want to delete: ', indent=10)
    dpg.add_combo(label='Api Name', indent=10, items=[], tag='del_api_name')
    dpg.add_button(label='delete', width=150, indent=10)

# 主菜单
with dpg.viewport_menu_bar():
    with dpg.menu(label='API'):
        dpg.add_menu_item(label="add", indent=5)
        dpg.add_menu_item(label="delete", indent=5)
    with dpg.menu(label='Group'):
        dpg.add_menu_item(label="add", indent=5)
        dpg.add_menu_item(label="delete", indent=5)


dpg.create_viewport(title='Config Panel', height=800, width=800)
dpg.show_viewport()

dpg.setup_dearpygui()
dpg.start_dearpygui()

dpg.destroy_context()
