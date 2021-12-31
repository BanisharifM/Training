import React, { Component } from "react";
import { getMovies } from "./services/fakeMovieService";
import "bootstrap/dist/css/bootstrap.css";

class Dively extends Component {
  state = {
    movies: getMovies()
  };
  handleClick(movie) {
    const movies = this.state.movies.filter(m => m._id !== movie._id);
    this.setState({ movies });
  }
  handleReset = () => {
    this.setState({ movies: getMovies() });
  };
  render() {
    const { length: count } = this.state.movies;
    if (count === 0)
      return (
        <React.Fragment>
          <p>There is no Movie to show</p>
          <button
            className="btn btn-secondary btn-sm"
            onClick={this.handleReset}
          >
            Reset
          </button>
        </React.Fragment>
      );
    return (
      <React.Fragment>
        <p>There is {count} Movies to show </p>
        <table className="table">
          <thead>
            <tr>
              <th>Title</th>
              <th>Genre</th>
              <th>Stock</th>
              <th>Rate</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {this.state.movies.map(movie => (
              <tr key={movie._id}>
                <td>{movie.title}</td>
                <td>{movie.genre.name}</td>
                <td>{movie.numberInStock}</td>
                <td>{movie.dailyRentalRate}</td>
                <td>
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => this.handleClick(movie)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </React.Fragment>
    );
  }
}

export default Dively;
