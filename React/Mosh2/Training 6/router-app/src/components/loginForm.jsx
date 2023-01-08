import React from "react";

class LoginFrom extends React.Component {
  state = {
    inputVal: "",
  };
  username = React.createRef();
  handleInputChange = (e) => {
    this.setState({ inputVal: e.target.value });
    console.log(this.username.current.value);
  };
  render() {
    return (
      <div>
        <h1>Login</h1>;
        <input ref={this.username} onChange={this.handleInputChange} />
        <p>{this.state.inputVal}</p>
      </div>
    );
  }
}

export default LoginFrom;
