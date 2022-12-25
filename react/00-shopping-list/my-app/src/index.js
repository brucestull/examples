import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class ShoppingList extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}:</h1>
        <ul>
          <li>Kat Fud, Of course!</li>
          <li>Scrubbing</li>
          <li>Catnip</li>
        </ul>
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ShoppingList name="Dezzi" />
  </React.StrictMode>
);