import { useEffect, useState } from "react";
import Parser from 'rss-parser';

function FeedComponent() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/feed")
      .then(res => {
        if (!res.ok) throw new Error("Network response was not ok");
        return res.json();
      })
      .then(json => {
        setData(json);
        setLoading(false);
      })
      .catch(err => {
        setError(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error loading feed</p>;
  
  return ( 
    <marquee>
      <div>
        {data["entries"].map(item => (
            <span key={item.id}><a href={item.link}>{item.title}</a> * </span>
        ))}
      </div>
    </marquee>
  );

}

export default FeedComponent;
