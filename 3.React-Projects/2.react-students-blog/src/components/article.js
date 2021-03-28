import React, {useState} from 'react';

function Article(props) {
    const [title, setTitle] = useState(props.articleTitle);

    const handlerChangeTitle = (event) => {
        setTitle(event.target.value);
    }

    return (
        <div className="card full-width">
            <h1
                onClick={props.changeColor}
                style={{ color: props.articleTitleColor }}>
                {title}
            </h1>
            
            <p>{props.children}</p>
            <p><b>You can change the article title here:</b></p>
            
            <input onChange={(e) => handlerChangeTitle(e)} type="text" value={title}></input>
        </div>
    );
}

export default Article;