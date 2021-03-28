import './App.css';
import Title from './components/title'
import List from './components/list'
import studentsListData from './data/students-list'
import Subtitle from './components/subtitle'
import ListArticles from './components/list-articles';


function App() {
    return (
    <div>
        <Title title='STUDENTS CODECOOL' />
        <Subtitle studentsLength = {studentsListData.length} />
        <List />
        <Title title='BLOG ARTICLES' />
        <ListArticles />
    </div>
    );
}

// obiect = { name: roxana }  => obiect.name = roxana

export default App;
