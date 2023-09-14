import React from "react";
import {createRoot} from "react-dom/client";
// import "./styles.css";

import App from "./components/App.jsx";

const root = createRoot(document.getelementById("root"));
root.render(<App/>);