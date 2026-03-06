export default function ScoreIndicatorBar({ width, score, color, player }) {
  const containerStyle = {
    width: `${width}%`,
  };

  return (
    <div className="score-indicator-bar-container" style={containerStyle}>
      <div className="score-indicator-bar" style={{ backgroundColor: color }}>
        {/* This score display decision is just for win page proof of concept  */}
        {score}
      </div>
      <h4>{player.display_name}</h4>
    </div>
  );
}
