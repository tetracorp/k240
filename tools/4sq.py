#!/usr/bin/env python
#
# make single-square k240 building sprites into four-square

from PIL import Image

bldgs = [
  "kll_data_hive.gif",
  "kll_power_converters.gif",
  "kll_queens_chamber.gif",
  "kll_ship_construction_factory.gif",
  "ore_command_bunker.gif",
  "ore_launch_facility.gif",
  "ore_turbine_array.gif",
  "axz_propulsion_unit.gif",
  "axz_reactor.gif",
  "axz_spacecraft_dock.gif",
  "axz_strategy_control.gif",
  "tyl_control_centre.gif",
  "tyl_fleet_factory.gif",
  "tyl_power_collector.gif",
  "tyl_thrusters.gif",
  "rig_deep_space_probes.gif",
  "rig_ground_dock.gif",
  "rig_reactor_core.gif",
  "rig_strategic_bunker.gif",
  "swi_brain.gif",
  "swi_docking_portal.gif",
  "swi_surge_generator.gif",
  "swi_tractor_generator.gif",
  "swi_tractor_generator.gif",
]

for bldg in bldgs:
  # Open the original image
  original_image = Image.open(bldg).convert("RGBA")

  # Calculate the size of the new image with borders
  border_size = (16, 0, 16, 16)  # left, top, right, bottom
  new_image_size = (original_image.width + border_size[0] + border_size[2],
                    original_image.height + border_size[1] + border_size[3])

  # Create a new transparent image with borders
  edited_image = Image.new("RGBA", new_image_size, (0, 0, 0, 0))
  edited_image.paste(original_image, (border_size[0], border_size[1]))

  # Paste the original image multiple times at different offsets
  offsets = [(0, 0), (16, 8), (-16, 8), (0, 16)]
  for offset in offsets:
    edited_image.alpha_composite(original_image, (border_size[0] + offset[0], border_size[1] + offset[1]))

  # Save the edited image
  new_name = bldg.replace(".gif","_4sq.gif")
  edited_image.save(new_name)
