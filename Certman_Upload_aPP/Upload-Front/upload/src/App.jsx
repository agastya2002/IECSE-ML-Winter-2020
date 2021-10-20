import React, { useState } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import SingleImage from "./components/SingleImage/SingleImage";
import Home from "./components/Home/Home";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path="/home" exact component={() => <Home />} />
          <Route path="/single-image/:_id" exact component={() => <SingleImage />} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
