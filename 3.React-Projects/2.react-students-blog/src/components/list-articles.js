import Article from './article';
import Button from './button';
import React, {useState} from 'react';

function ListArticles(props) {
    const [articleTitleColor, setArticleTitleColor] = useState('black');

    const changeTitleColor = (color) => {
        setArticleTitleColor(color);
    }
    

    return (
        <div className="articles">
            <Button changeColor = {() => changeTitleColor('red')} buttonName="Toggle color"></Button>
            <Article
                articleTitle="Article 1"
                articleTitleColor={articleTitleColor}
                changeColor={() => changeTitleColor('blue')}>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</Article>
            
            <Article
                articleTitle="Article 2"
                articleTitleColor={articleTitleColor}
                changeColor={() => changeTitleColor('green')}>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</Article>
            
            <Article
                articleTitle="Article 3"
                articleTitleColor={articleTitleColor}
                changeColor={() => changeTitleColor('purple')}>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</Article>
        </div>
    );
}

export default ListArticles;