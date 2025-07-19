🌍 3D Earth and Moon Simulation
This project is a web-based 3D simulation of the Earth and its orbiting Moon, built using the Three.js JavaScript 3D library. It visually represents the Earth's rotation on its axis and the Moon's revolution around it, providing a simple yet interactive planetary system model that runs directly in the browser.

🌐 Overview
The simulation features:

A rotating Earth with realistic texture mapping.

A Moon orbiting the Earth on a circular path.

Dynamic lighting to simulate sunlight and shadow.

Smooth animations using requestAnimationFrame for performance.

This is a JavaScript recreation of a VPython project. The original Python version used vpython for real-time 3D graphics, but this web-based version makes the simulation easily accessible in any modern browser using HTML, CSS, and JavaScript, with no installations required.

🧠 Technologies Used
Three.js: Handles the 3D rendering, lighting, camera, and object creation.

HTML & CSS: Provides the structure and layout.

JavaScript: Controls the logic, animation, and interaction.

Textures: Earth texture from Three.js examples; Moon texture can be customized or replaced with a fallback color.

🚀 Features
Realistic Earth model: The Earth uses a high-resolution texture mapped onto a 3D sphere, rotating around its Y-axis to simulate daily rotation.

Orbiting Moon: The Moon moves in a circular orbit using trigonometric functions (cos and sin) to calculate its position relative to the Earth. It also rotates slightly to create a dynamic look.

Dynamic Lighting: A point light simulates the Sun, casting light onto the Earth and Moon for depth and realism.

Responsive Canvas: The scene is rendered on a canvas of 1075x475 pixels, with no scrollbars or browser UI interfering.

🧪 How It Works
The Earth is created as a sphere mesh with a loaded texture, placed at the center of the scene. The Moon is a smaller sphere that updates its position each frame to move in a circular path around the Earth. Lighting is added via a point light source to give both objects realistic shading. The animate() function continuously updates the rotation and position of the objects and renders the scene.

🔧 How to Run
Just open the index.html file in your browser, or paste the code into a service like CodePen, JSFiddle, or Glitch. No backend or server is required — this is a completely client-side simulation.

📦 Use Cases
Educational tools for astronomy and planetary science

Visual demos for JavaScript and Three.js learners

Interactive art and 3D simulations

Web-based science projects

📁 Folder Structure
css
Copy
Edit
index.html  → Main simulation code
textures/   → (Optional) Folder to store Earth/Moon textures
✨ Credits
Three.js for the 3D engine

NASA and Three.js community for texture resources

