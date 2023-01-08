import React, { Component } from "react";
import Counter from "./counter";

class Counters extends Component {
  state = {
    values: [
      { id: 1, value: 0 },
      { id: 2, value: 4 },
      { id: 3, value: 0 },
      { id: 4, value: 0 },
    ],
  };
  handleDelete = (id) => {
    const values = this.state.values.filter((value) => value.id !== id);
    this.setState({ values: values });
  };
  render() {
    return (
      <React.Fragment>
        {this.state.values.map((counter) => (
          <Counter
            key={counter.id}
            value={counter.value}
            onDelete={() => this.handleDelete(counter.id)}
          />
        ))}
      </React.Fragment>
    );
  }
}

export default Counters;
