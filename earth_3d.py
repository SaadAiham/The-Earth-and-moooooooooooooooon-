from vpython import sphere, vector, textures, rate, canvas, color, cos, sin

scene = canvas(width=1075, height=475, center=vector(0,0,0), background=color.black)

earth = sphere(pos=vector(0,0,0), radius=1, texture=textures.earth)

# moon with texture fallback to gray color if texture doesn't load
try:
    moon = sphere(pos=vector(2,0,0), radius=0.27, texture="moon.jpg")
except:
    moon = sphere(pos=vector(2,0,0), radius=0.27, color=color.gray(0.7))

angle = 0
scene.camera.pos = vector(0, 0, 5)
scene.camera.axis = vector(0, 0, -5)

while True:
    rate(60)
    earth.rotate(angle=0.01, axis=vector(0,1,0))
    angle += 0.02
    moon.pos = vector(2*cos(angle), 0, 2*sin(angle))
    moon.rotate(angle=0.01, axis=vector(0,1,0))
