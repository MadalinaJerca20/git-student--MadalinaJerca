import { Card } from "react-bootstrap";
import { Button } from 'react-bootstrap'

const CardProducts = (prop) => {
    return (
        <div className="productCard">
            <Card style={{ width: '18rem' }} className="box">
                <Card.Img variant="top" src={prop.data.image} fluid/>
                <Card.Body className="cardBody">
                    <Card.Title>{prop.data.name}</Card.Title>
                    <Card.Text>
                        {prop.data.description}
                    </Card.Text>
                    <Card.Text>
                        {prop.data.price}
                    </Card.Text>
                    <Button variant="primary" class="prod-btn">Go somewhere</Button>
                </Card.Body>
            </Card>
        </div>
    );
};

export default CardProducts;



















// <div className="card-container">
        //     <div className="card-image">{props.data.image}</div>
        //     <div className="card-body">
        //         <h3>{props.data.name}</h3>
        //         <p>{props.data.description}</p>
        //         <p className="price">{props.data.price}</p>
        //         <a href="#" className="btn">Add to cart</a>
        //     </div>
        // </div>