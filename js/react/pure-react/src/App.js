import React from "react";
import { render } from "react-dom";
import Pet from "./Pet.js";

// like blueprint/stamp
const App = () => {
  return React.createElement(
    "div",
    { id: "something-important" },
    React.createElement("h1", {}, "Adopt Me!")
  );
};

render(React.createElement(App), document.getElementById("root"));
