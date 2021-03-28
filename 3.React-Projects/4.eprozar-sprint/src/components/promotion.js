import { Card } from "react-bootstrap";

function Promotion() {
    return (
        <section class="promotion">
            {/* <h2>Don't miss today's hot deal!</h2> */}
            <Card style={{ width: '30rem' }} className="box-promo">
                <Card.Img variant="top" src="https://picsum.photos/id/1045/500/500/" alt="Small Frozen Bacon"/>
            </Card>
            <Card.Body className="box-body">
                    <Card.Title className="promo-title">SMALL FRONEZ BACON</Card.Title>
                    <Card.Text className="promo-text">
                        Exercitatioem soluta vero quos omnis nesciunt lorem ipsum lorme lorem.
                    </Card.Text>
                    <Card.Text className="promo-text">
                        <span className="price">$19.00</span>    
                        <span> only on </span>
                        <span className="date">25 March</span>
                        <a href="#" class="promo-btn">BUY NOW</a>   
                </Card.Text>
                              
                </Card.Body>
        </section>
    );
}

export default Promotion;