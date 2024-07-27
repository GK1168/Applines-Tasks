import Cards from './imageCard.js'
import './imageList.css'
import image1 from '../../assets/image1.png'
import image2 from '../../assets/image2.png'
import image3 from '../../assets/image3.png'
import image4 from '../../assets/image4.png'

export default function Images() {
    const images_list = [
        {
            image: image1,
            title: 'Paris',
            description: 'paris is the department with the highest proportion of highly educated people',
        },
        {
            image: image2,
            title: 'Bangkok',
            description: 'paris is the department with the highest proportion of highly educated people',
        },
        {
            image: image3,
            title: 'Malaysia',
            description: 'paris is the department with the highest proportion of highly educated people',
        },
        {
            image: image4,
            title: 'Indonesia',
            description: 'paris is the department with the highest proportion of highly educated people',
        }
    ];
    return (
        <div className="row menu-card">
            <div className="col-3"><Cards image={images_list[0].image} title={images_list[0].title} description={images_list[0].description} /></div>
            <div className="col-3"><Cards image={images_list[1].image} title={images_list[1].title} description={images_list[1].description} /></div>
            <div className="col-3"><Cards image={images_list[2].image} title={images_list[2].title} description={images_list[2].description} /></div>
            <div className="col-3"><Cards image={images_list[3].image} title={images_list[3].title} description={images_list[3].description} /></div>
        </div>
    );
}