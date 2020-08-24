const canvasSketch = require("canvas-sketch");

const settings = {
	dimensions: [2048, 2048]
	// orientation: "landscape",
	// units: "in",
	// pixelsPerInch: 300
};

const sketch = () => {
	return ({ context, width, height }) => {
		context.fillStyle = "salmon";
		context.fillRect(0, 0, width, height);

		context.beginPath();
		context.arc(width / 2, height / 2, width * 0.2, 0, Math.PI * 2, false);
		context.fillStyle = "red";
		context.fill();

		context.lineWidth = width * 0.05;
		context.strokeStyle = "green";
		context.stroke();
	};
};

canvasSketch(sketch, settings);
