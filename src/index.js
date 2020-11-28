import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

class MyForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      age: null,
      errormessage: ''
    };
  }//constructor
  myChangeHandler = (event) => {
    let nam = event.target.name;
    let val = event.target.value;
    let err = '';
    if (nam === "age"){
      if (!Number(val)){
        err = <strong> Age must be digits </strong>;
      }
    }
    this.setState({errormessage: err});
    this.setState({[nam]: val});
  }
  render() {
    return(
      <form>
        <h2>Hello {this.state.username} {this.state.age}</h2>
        <p> name:</p> 
        <input type='text' name='username' onChange={this.myChangeHandler} />
        <p> age: </p>
        <input type='text' name='age' onChange={this.myChangeHandler} />
        {this.state.errormessage}
      </form>
    );
  }
}
ReactDOM.render(<MyForm/>, document.getElementById('myform6'))

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
