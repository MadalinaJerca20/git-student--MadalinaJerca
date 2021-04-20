import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { data, getRecipeById } from "../data";

function Home() {
  return (
    <Carousel showArrows={true} showThumbs={true}>
      {data.map((e, index) => (
        <div key={index}>
          <img className="w-100" src={e.image} alt={e.title} />
          <p className="legend">{e.title}</p>
        </div>
      ))}
    </Carousel>
  );
}

export default Home;
