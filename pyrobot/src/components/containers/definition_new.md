## general properties

```
general_id : string
```
internal identifier, must be unique and should only contain Letters and Numbers. Preferably in the form 

[3C:manufacturer][4C:number][addletters]

e.g. `COR3569b`. This will be added to the python class as variables for direct access in the form `Plates.COR3569b`

```
general_checked : bool (default=false)
```
if true the plate entry is considered correct and can be safely used

```
general_name : string
```
a readable representation
```
general_name_short : string (optional)
```
a short readable representation 

```
general_description : string
```
a long description of the plate

```
general_comment : string
```
comments of any kind
    
```
general_image : string (optional)
```
a file name without actual path that links to a picture (preferrably png) the shows the carrier

#### manufacturer properties

```
    manufacturer_name : string
```
a string identifying the manufacturer. Try to be consistent with the naming

```
    manufacturer_url : url (optional) (default=http://)
```
the url to the website of the manufacturer

```
    manufacturer_product_url : url (optional) (default=http://)
```
url to the product itself

```
    manufacturer_number : string
```
the manufacturers part number for reordering, etc

```
    manufacturer_pdf_url : url (optional) (default=http://)
```
url to a pdf with product specifications

#### id properties

```
    id_momentum : string
```
an identifier that allows to specify the correct container type in Momentum, e.g. '4titude 4ti_0223'

```
    id_evo : string
```
an identifier that allows to specify the correct microplate labware in EVOware, e.g. just the name of the labware

```
    id_infinite : string
```
an identifier that allows to specify the correct plate type in i_control, e.g. the name of the corresponding .pdfx file

```
    id_barcode : enum {A, B, C, D, E, F, G, H, J, K, L, M, N, P, R, T, U, W, X, Y, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```
identifying letter used in the barcode schema. Should only be a single capital letter
        
#### plate properties		

```
    plate_bottom_read : bool (computed)
```
true if plate can be read from the bottom

```
    plate_color : enum {clear, black, white, red} (free) (default=black)
```
the plate color which might be important in the infinite because of light scattering - black is considered good for fluorescence while white is good for high luminescence. Red looks nice :)

```
    plate_type : enum {96, 384, 1536, 24, 6, 3} (computed)
```
the plate type 96, 384 or 1536, given by 'plate_rows' * 'plate_columns'

```
    plate_material : enum {Polypropylene, Polystyrene} (optional) (free)
```
a string describing the material the plate / not the well treatment is made of, e.g. polypropylene, polystyrene

```
    plate_rows : int (default=8)
```
number of wells in y_direction / rows, usually 8, 16 or 32

```
    plate_columns : int (default=12)
```
number of wells in x_direction / columns, usually 12, 24 or 48

```
    plate_numbering : enum {row, column} (default=row)
```
defines in which direction wells are counted. This is only for convenience and is probably obsolete

```
    plate_height : float [mm] (default=14.4)
```
height of the container, around 10_30 mm

```
    plate_length : float [mm] (default=127.76)
```
length of the container (x_direction, long side), around 125 mm

```
    plate_width : float [mm] (default=85.48)
```
width of the container (y_direction, short side), around 80 mm

```
    plate_sterile : bool (default=false)
```
if true the plate is considered to be sterile and packaged as such

#### flange properties

```
    flange_type : enum {short, medium, tall, interrupted, dual, none}
```
The SBS specifications list 5 types for flanges. Which are briefly defined here. The heights have a tolerance of  \pm 0.38 mm. Therefore no field for the actual height is given.
When in doubt choose a higher one to provide correct picking and placement of labels.

  1. short: height : 2.41 mm
  2. medum : height : 6.10 mm
  3. tall : height: 7.62 mm
  4. interrupted : height : 2.41 mm (like low) and has an interruption (change of height) centered at both long sides. The distance from the interruption to the sides of the plate should be at least 47.8 mm on each side. The height of the interruption should not exceed 6.85 mm
  5. dual : means short on the short sides 2.41 mm and tall on the long sides 7.62 mm.
  6. none : not standard, just no flange, like for selfmade parts

```
    flange_height_short : float [mm] (computed) 
```
distance between bottom of the plate and end of the flange on the short side. the height gives the actual height including the ledge. I am actually not sure what flange height for the Infinite means but I guess thats this coincides with the flange height. At least numbers kind og match. This might be listed in a newer manual of i-control 1.10.
This defines the region where the orbitor or roma canNOT or should NOT grip. for dual mode this refers to the short side (the y-direction in the normal orientation). Short side height is given is flange_height_short.
height of the flange of the short side. Only necessary is type is dual. Otherwise it is the same as flange_height_long

```
    flange_height_long : float [mm] (computed) 
```
height of the flange of the long side. Only necessary is type is dual. Otherwise it is the same as flange_height_short. See flange_height_short or flange_type for more details

```
    flange_width : float [mm] (optional)
```
the thickness of the flange, which is supposed to be at least 1.27 mm. Is not needed for gripping since the gripping is usually not on the flange.

```
	flange_dropstate : bool (computed)
```
is true if 'flange_type' requires to drop the plate by 5mm in the VCode to correctly place a barcode label

#### stacking properties

```
    stacking_above : bool (default=true)
```
true if plates are allowed to be put on top (above)

```
    stacking_below : bool (default=true)
```
true if plates are allowed to be put under this plate (below)

```
    stacking_plate_height : float [mm]
```
Effective height if container is stacked. Note that this height is for the container itself, if it is stacked upon another plate. So, if two plates are stacked, the lower one has full height and the top one uses its stacking_height

```
    stacking_plate_shift : float [mm] (computed)
```
distance the plate is lower when stacked. Should be plate_height - stacking_plate_height 

#### well properties

```
    well_size : enum {full, half, low, deep} (default=full) (computed)
```
This is for convenience. In principle all well parameters should allow to determine the area and thus if it is a half of full. Also low should be deducible from well_depth 

```
    well_coating : enum {none, nonbonding} (default=none) (free)
```
coating material of the well

```
    well_bottom_type : enum {clear, solid, UV} (free)
```
material type of the bottom of the well

```
    well_evo_profile : enum {flat, round, ushape, vshape, octo, unknown} (computed)
```
bottom shape of a well. Here EVO and Infinite (both Tecan!!!) are inconsistent. 
Infinite allows for round and U_shape, which seem to be different, while EVO only defines 
round which seems to match Infinites U_shape. We wills stick with the Infinite definition 
and treat round and U_shape both as U_shape in the EVO. This might reduce the 
actual volume a little. In general we will assume that

  1. flat : is just flat. 
  2. u : means a (upto) half sphere that matches with outgoing straight walls
  3. v : means straight lines from the center in an angle of 'well_profile_angle'
  4. round : means a half_sphere that cuts off at 45 degrees and V_shape means an angle of 45 degrees. We also assume for now that only flat bottoms allow for rectangular well shapes. Also, in standard plates wells are square or round. And momentum doesn't care - no pipetting...
  5. octagon : for Corning, like 'v' but allows for a bottom_diameter larger than zero. This way it looks like an octagon.
This means that (in principle) we could remove 'v' and 'flat'

```
    well_diameter_bottom : float [mm]
```
the inner diameter of the bottom shape. For vshape and flat wells this is ignored. For round it describes the radius of the round surface and for angle it is the diameter of the flat part.

```
    well_diameter_middle : float [mm]
```
the inner diameter of the middle of the well where top and bottom meet.

```
    well_diameter_top : float [mm]
```
inner diameter of a well. If non-symmetric then this is the shorter side

```
    well_diameter_top_y : float [mm] (optional) (empty=well_diameter_top)
```
inner diameter of the y side of a well. This is only needed if a well is not square. This is normally ignored and is only need for troughs or other special containers.

```
	well_aspect : float (computed)
```
Gives the ratio between x and y diameter of a well.

```
	well_bottom_profile : enum {flat, round, angle, vshape}
```
Defines the vertical profile of the bottom part, the tip. We have flat which is just a flat bottom, vshape which is a straight line from the center. Angle is flat and then changes to a tilted line. Round is first round with a fixed radius and then changes to a straight line. All of these profiles hit the top profile in the middle and we assume this is if we cut a well in the center of the y-dimension so that we watch the x-dimension.

```
	well_top_profile : enum {straight}
```
Defines the vertical profile of the top of the well. So far this is always a straight line. See well_bottom_profile for more details.

```
	well_bottom_shape : enum {round, square}
```
Defines the horizontal shape of the well at the bottom. We have round and square.
 
```
	well_top_shape : enum {round, square, nodded, octo}
```
Defines the horizontal shape of the well at the top. We have round and square.

```
    well_top_nodging : float [mm] (optional)
```
Only for wells that are nodged or octo. It gives the size of the nodge_kink in the corners of the well. Nodging seems to be used for 384 / 1536 plates to increase stability at the well joints. This rounds the corners and decreases the possibility that substances get stuck in the edges. 

```
	well_middle_position : float [mm]
```
Position of the middle where top and bottom meet. Measured from the top and is thus equal to well_top_height.

```
	well_top_height : float [mm] (computed)
```
Height of the top-part of the well. This is the distance from the top part of the plate to the height where top and bottom meet.

```
	well_bottom_height : float [mm] (computed)
```
Height of the bottom-part of the well. This is the distance from the lowest part of the plate to the height where top and bottom meet. bottom and top height have to add up to the total well_depth.

```
    well_position_first_x : float [mm]
```
x position of the center of A1

```
    well_position_first_y : float [mm]
```
y position of the center of A1

```
    well_distance_x : float [mm] (optional)
```
x distance between two neighboring centers. Should be 9.00mm, 4.50mm or 2.25mm. 

```
    well_distance_y : float [mm] (optional) (empty=well_distance_x)
```
x distance between two neighboring centers. Should be 9.00mm, 4.50mm or 2.25mm.  If not specified then the same as 'well_distance_x'

```
    well_position_last_x : float [mm] (computed)
```
x position of the center of H12 / P24 given by 'well_postition_first_x' + (plate_rows - 1) * 'well_distance_x'

```
    well_position_last_y : float [mm] (computed)
```
y position of the center of H12 / P24 given by 'well_postition_first_y' + (plate_columns - 1) * 'well_distance_y'

```
    well_volume_total : float [ul] (computed)
```
the total volume of a well that is computed using the size and shape of the well

```
    well_area : float [mm x mm] (computed)
```
the area of the well on the opening

```
    well_depth : float [mm]
```
Distance between the lowest point in a well and the top of the well / plate

```
    well_volume_max : float [ul]
```
maximal volume to be used to ensure safe transport of the plates without spilling. Must be less than well_volume_total

```
    well_volume_working_min : float [ul]
```
minimal recommended working volume where the well makes sense to be used.

```
    well_volume_working_max : float [ul]       
```
maximal recommended working volume where the well makes sense to be used.

#### lidding properties         

```
    lid_allowed : bool (default=True)
```
if a lid is allowed on this plate

```
    lid_offset : float [mm] (default=0.0)
```
relative z_shift for lid gripping compared to container gripping. Negative values mean lower/down. Sign might be different for EVO and momentum 

```
    lid_plate_height : float [mm]
```
height of the plate including its lid
            
#### Momentum specific properties

```
    momentum_grip_force : int [%]
```
force applied for gripping with the orbitor

The following defines a transformation by (x,y,z) translation and some rotation using 'quaternions' which seems odd in the momentum 'low'/'high'/'custom' scheme. Default : ((0,0,0), (0,0,0), 0), momentum shows Identity

```
    momentum_offsets_low_lidded_plate : float [mm] (default=0.0)
```
relative add to plate_z position to be used in the momentum 'low'/'high'/'custom' scheme.

```
    momentum_offsets_low_lidded_lid : float [mm] (default=0.0)
```
relative add to lid_grip z_position to be used in the momentum 'low'/'high'/'custom' scheme. 

```
    momentum_offsets_low_grip_transform : custom (default=Identity)
```
a grip transformation used in the momentum 'low'/'high'/'custom' scheme of format ((float, float, float), (float,float,float), float)

```
    momentum_offsets_high_lidded_plate : float [mm] (default=0.0)
```
relative add to plate_z position to be used in the momentum 'low'/'high'/'custom' scheme.

```
    momentum_offsets_high_lidded_lid : float [mm] (default=0.0)
```
relative add to lid_grip z_position to be used in the momentum 'low'/'high'/'custom' scheme.

```
    momentum_offsets_high_grip_transform : custom (default=Identity)
```
a grip transformation used in the momentum 'low'/'high'/'custom' scheme of format ((float, float, float), (float,float,float), float)

```
    momentum_offsets_custom_lidded_plate : float [mm] (default=0.0)
```
relative add to plate_z position to be used in the momentum 'low'/'high'/'custom' scheme. 

```
    momentum_offsets_custom_lidded_lid : float [mm] (default=0.0)
```
relative add to lid_grip z_position to be used in the momentum 'low'/'high'/'custom' scheme. 

```
    momentum_offsets_custom_grip_transform : custom (default=Identity)
```
a grip transformation used in the momentum 'low'/'high'/'custom' scheme of format ((float, float, float), (float,float,float), float)

            
#### Evo specific properties. Not used yet because there is no direct access to the labware in EVOware.

```
    evo_plate_grip_force : int [%] (default=75)
```
force applied for grippin a plate with the roma

```
    evo_lid_grip_force : int [%] (default=60)
```
force applied for gripping a lid with the roma

```
    evo_lid_grip_narrow : float [mm] (default=92.0)
```
gripper opening of the roma used for picking the lid in narrow orientation

```
    evo_lid_grip_wide : float [mm] (default=135.0)
```
gripper opening of the roma used for picking the lid in wide orientation