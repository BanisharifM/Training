import React, { Component } from "react";
import Counters from "./components/counters";
import Navbar from "./components/navbar";

class App extends Component {
  constructor() {
    super();
    console.log("App - Constructor");
  }
  componentDidMount() {
    console.log("App - Mounted");
  }
  state = {
    counters: [
      { id: 1, value: 0 },
      { id: 2, value: 1 },
      { id: 3, value: 2 },
      { id: 4, value: 3 }
    ]
  };
  handleRefresh = () => {
    this.setState({
      counters: [
        { id: 1, value: 0 },
        { id: 2, value: 1 },
        { id: 3, value: 2 },
        { id: 4, value: 3 }
      ]
    });
  };
  handleIncrement = counter => {
    const counters = [...this.state.counters];
    const index = counters.indexOf(counter);
    counters[index].value++;
    this.setState({ counters });
  };
  handleDecrement = counter => {
    const counters = [...this.state.counters];
    const index = counters.indexOf(counter);
    counters[index].value--;
    this.setState({ counters });
  };
  handleReset = () => {
    const counters = this.state.counters.map(c => {
      c.value = 0;
      return c;
    });
    this.setState({ counters });
  };
  handleDelete = id => {
    let counters = this.state.counters.filter(item => item.id !== id);
    this.setState({ counters });
  };
  render() {
    console.log("App - Renderd");
    return (
      <React.Fragment>
        <Navbar
          totalCounter={this.state.counters.filter(c => c.value > 0).length}
        />
        <Counters
          counters={this.state.counters}
          onRefresh={this.handleRefresh}
          onReset={this.handleReset}
          onIncrement={this.handleIncrement}
          onDecrement={this.handleDecrement}
          onDelete={this.handleDelete}
        />
      </React.Fragment>
    );
  }
}

export default App;
