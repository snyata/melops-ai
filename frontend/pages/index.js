import IntroAnimation from '../styles/IntroAnimation';

// Using getStaticProps in pages/index.js for SSG
export async function getStaticProps() {
  const res = await fetch('https://synavate.tech/api/v1/test');
  const data = await res.json();

  return {
    props: {
      data,
    },
  };
}

export default function Home() {
  return (
    <>
      <IntroAnimation />
      {/* The rest of your page content */}
    </>
  );
}