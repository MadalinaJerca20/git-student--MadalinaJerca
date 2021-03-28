import React from 'react';

function Button(props) {
    return (
        <button onClick={props.changeColor}>{props.buttonName}</button>
    );
}

export default Button;