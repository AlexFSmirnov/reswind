# ResWind
ResWind is library for pygame, which allows you to create a window that can be resized without distorting the main surface aspect ratio.
## Example
Here you can find an example (example.py), that will draw a circle in a resizable window.

![Normal circle](/images/1.png)

If you resize the window, you will see, that the circle doesn't turn into an oval but stays in it's form and moves to the center of the window.

![Resized circle](/images/2.png)

## Usage
First of all import this library.
```python
import reswind
```
To create a ResWind window simply use:
```python
window = reswind.ResizableWindow(initial_size,
                                 main_size,
                                 gap_fill_type  = "solid_color",
                                 gap_fill_color = (0, 0, 0),
                                 gap_steps      = 100,
                                 draw_lines     = True,
                                 lines_color    = (100, 100, 100),
                                 smoothscale    = True)
```
Here **initial_size** and **main_size** are the only two required parameters. Let's go through all parameters now and see, what they are used for:
 * **initial_size**   - the size of the window, when it is just created.
 * **main_size**      - the size of the main surface, which you don't want to be distorted. You will later use this surface to draw on it and its real size will stay fixed and independent of the surface that is displayed *(e.g. if main_size is (100, 100) but you resize the window to fit a (500, 500) screen, the window.main_surface.get_at((100, 100)) will still return the bottom left corner)*.
 * **gap_fill_type**  - how the gaps between the main surface and the window frame will be filled. Possible values:
    * *"solid_color"* - the gaps will be filled with a solid color (you can select it using the next parameter).
    * *"gradient_up"* - the gaps will be filled with a gradient, which becomes **brighter** on the way from the main surface to the frame.
    * *"gradient_down"* - the gaps will be filled with a gradient, which becomes **darker** on the way from the main surface to the frame.

* **gap_fill_color**  - the start color of the gap. If it is solid - whole gap will be colored with this color, if it is a gradient - it will become darker or brighter on it's way to the frame.
* **draw_lines**      - if it is True, two lines will appear between the gap and the main surface. Sometimes it looks good.
* **lines_color**     - the color of those lines.
* **smoothscale**     - as I said, the main surface will scale anywhay, so this parameter is responsible for the way, how the surface will be scaled.

In order to do all the computations and resize itself, the window has to catch the "VIDEORESIZE" event in your event-tracker loop:
```python
while True:
    event = pygame.event.wait()
    ...

    # Here:
    window.updateSize(event) 

    ...
```
