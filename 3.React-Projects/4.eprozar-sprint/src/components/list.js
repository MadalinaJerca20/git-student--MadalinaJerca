import CardProducts from "./card"
import productList from '../data/productList'

function List() {
    return (
        <div className="grid productCards">
            {
            productList.map((product) => (<CardProducts data = {product} />))
            }
        </div>
    );
}

export default List;

