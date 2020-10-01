import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.css";
class Counter extends Component {
  constructor() {
    super();
    // this.handleIncreament = this.handleIncreament.bind(this);
  }
  state = {
    count: 0,
    tags: ["tag1", "tag2", "tag3"]
  };
  handleIncreament = () => {
    this.setState({ count: this.state.count + 1 });
  };
  handleDerease = () => {
    let count = this.state.count;
    this.setState({ count: count === 0 ? 0 : count - 1 });
  };
  render() {
    return (
      <div>
        <span className={this.getBadgeClass()}>{this.formatCount()}</span>
        <button
          className="btn btn-secondary btn-sm m-2"
          style={{ fontWeight: "bold" }}
          onClick={this.handleIncreament}
        >
          +
        </button>
        <button
          className="btn btn-secondary btn-sm m-2"
          style={{ fontWeight: "bold" }}
          onClick={this.handleDerease}
        >
          -
        </button>
        <ul>
          {this.state.tags.map(tag => (
            <li key={tag}>tag</li>
          ))}
        </ul>
      </div>
    );
  }

  getBadgeClass() {
    let spanState = "badge m-2 badge-";
    spanState += this.state.count === 0 ? "warning" : "primary";
    return spanState;
  }

  formatCount() {
    const { count } = this.state;
    return count === 0 ? "Zero" : count;
  }
}

export default Counter;

//  onclick={()=> this.handleIncreament(key)}
