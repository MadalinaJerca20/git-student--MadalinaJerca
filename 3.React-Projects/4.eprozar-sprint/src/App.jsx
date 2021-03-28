import productList from "./data/productList";
import Promotion from "./components/promotion.js"
import List from "./components/list.js"
import Footer from "./components/footer"

const App = () => {
    console.log(productList)
    return (
        <div>
            <Promotion />
            <List />
            <Footer />
        </div>
    );
};

export default App;