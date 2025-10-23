# shinretro revisited (ES-DE)
A port of the shinretro theme by [TiagraTT-Driver](https://github.com/TigraTT-Driver/shinretro) for ES-DE v3.0.

## **Preview**

| System View |
|----|
| ![16-9 system](https://github.com/RobZombie9043/shinretro-revisited-es-de/assets/77545967/ced45973-59c1-4456-9a07-b881d93c4d59) | 

| Gamelist View: Carousel | Gamelist View: Grid |
|----|----|
| ![16-9 carousel](https://github.com/RobZombie9043/shinretro-revisited-es-de/assets/77545967/c0967b7f-4abd-4d5c-a538-e54c31ba1222) | ![16-9 grid](https://github.com/RobZombie9043/shinretro-revisited-es-de/assets/77545967/7ff9a051-724b-4a2e-ab02-3b019df0d19f) |

## **Configuration Options**

- The theme has a simple set of options that can be changed directly from the UI Settings menu of ES-DE 
- `Theme Aspect Ratio` - sets the aspect ratio the theme will render at. If needed, this can be changed to match the aspect ratio of your screen (though it should happen automatically).
   - `16:9`, `16:10`, `4:3`, `1:1` and `19.5:9` are supported
- `Theme Variant` - sets the layout used for the gamelist view when media & metadata are scraped for your games.  There are 2 variants to choose from:
   - `Grid` - A grid game selection with detailed metadata.
   - `Carousel` - A carousel game selection with detailed metadata.
- `Theme Color Scheme` - sets the color scheme that is used for the overall theme on all views.  There are 4 built in color schems to choose from:
   - `Dark` - A dark grayscale color scheme.
   - `Light` - A light grayscale color scheme.
   - `SteamOS` - Based on the primary colors used in Steam OS.
   - `Shinretro Dark` - Based on the shinretro dark theme.
- `Theme Font Size` - enables you to change the size of the fonts displayed in the theme. There are 2 sizes to choose from:
   - `medium`
   - `large`

## **Theme Customization**

- Create a folder called `theme-customizations` in the main shinretro theme folder and then create a subfolder named `artwork` resulting in a folder structure `~ES-DE/themes/shinretro-revisited-es-de/theme-customizations/artwork/`
- Copy your custom carousel images to that `artwork` folder
- They should be named `${system.theme}.webp`, For example for `snes` you would create an image called `snes.webp`
  - Note that custom images only need to be supplied for the systems to be customized and the default system image will be used for any other systems.
  - The carousel images use an aspect ratio of 0.65:1 so if images that are provided use a different aspect ratio to this they will be cropped which may cut off parts of the image and not look good.
- Change the theme color scheme to one of the color schemes with `Custom` in the name and the artwork from the custom folder will be used.
 
## **Acknowledgements**

Based on original neoretrō theme by [Valentin MEZIN](https://github.com/valsou) and shinretro theme by [TigraTT-Driver](https://github.com/TigraTT-Driver) including use of system artwork.  

Custom sfx from shinretro theme by [RoeTaKa](https://www.youtube.com/channel/UCAbHcM41hzH9lku_3XqFYZg).  

Ported to ES-DE by [ant](https://github.com/anthonycaccese) and Rob Zombie.

Alekfull system artwork created by [fagnerpc](https://github.com/fagnerpc)

Android apps artwork - (https://wallpaperswide.com/android_robot_listening_to_music-wallpapers.html)  
Arcadia artwork - (https://arcadia.fun/)  
Emulators artwork - (https://wallpapers.com)  

Nexa Rust Slab Black Shadow 1 font by Fontfabric

