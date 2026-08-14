import "./style.css";

function App() {

return (

<div className="app">

<div className="sidebar">

<h2>🛡 AI Cybersecurity</h2>

<ul>

<li>Dashboard</li>
<li>Monitor</li>
<li>Threats</li>
<li>Alerts</li>
<li>Traffic</li>
<li>Scanner</li>
<li>Reports</li>
<li>Settings</li>

</ul>

<div className="protect">

<h1>87%</h1>

<p>Protected</p>

</div>

</div>


<div className="main">

<header>

<h1>AI Cybersecurity Threat Detector</h1>

<div className="status">

🟢 Protected

</div>

</header>


<div className="cards">

<div className="card red">

<h3>Total Threats</h3>

<h1>1248</h1>

</div>

<div className="card orange">

<h3>Alerts</h3>

<h1>23</h1>

</div>

<div className="card green">

<h3>Blocked</h3>

<h1>942</h1>

</div>

<div className="card purple">

<h3>Vulnerabilities</h3>

<h1>17</h1>

</div>

</div>


<div className="grid">

<div className="box">

<h2>Threat Overview</h2>

<img
src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3"
/>

</div>

<div className="box">

<h2>Threat Types</h2>

<div className="circle">

1248

</div>

</div>

<div className="box">

<h2>Network Traffic</h2>

<div className="graph">

<div className="line"></div>

</div>

</div>

</div>


<div className="table">

<h2>Recent Alerts</h2>

<table>

<tr>
<th>Type</th>
<th>Severity</th>
<th>Source</th>
</tr>

<tr>
<td>Malware</td>
<td>High</td>
<td>192.168.1.45</td>
</tr>

<tr>
<td>DDoS</td>
<td>Critical</td>
<td>45.76.12.8</td>
</tr>

<tr>
<td>Phishing</td>
<td>Medium</td>
<td>mail.fake.com</td>
</tr>

</table>

</div>

</div>

</div>

);

}

export default App;