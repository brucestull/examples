import React from 'react';
import ReactDOM from 'react-dom/client';

class ExampleComponent extends React.Component {
    render() {
        return <h1>Welcome, to the Render Simple React Component Example!</h1>;
    }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <ExampleComponent />
    </React.StrictMode>
);