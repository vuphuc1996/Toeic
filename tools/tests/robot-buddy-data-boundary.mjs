import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
const root=path.resolve(path.dirname(new URL(import.meta.url).pathname),'../..');
const buddy=fs.readFileSync(path.join(root,'assets/js/robot-buddy.js'),'utf8');
const insights=fs.readFileSync(path.join(root,'assets/js/robot-learning-insights.js'),'utf8');
const app=fs.readFileSync(path.join(root,'assets/js/app.js'),'utf8');
// The companion engine and aggregator must not directly access stores or remote services.
for(const source of [buddy,insights]){
  assert.doesNotMatch(source,/\b(?:indexedDB|localStorage|sessionStorage|fetch|XMLHttpRequest|WebSocket)\b/i,'Robot engine/aggregator must not directly access storage or network');
}
// Snapshot summaries require an explicit true preference; missing/false is disabled.
assert.match(app,/robotReadSettings\(\)\.learningInsightsEnabled===true/,'missing setting must remain off');
assert.match(app,/settings\.learningInsightsEnabled===true/,'insights generation must require explicit opt-in');
assert.match(app,/settings\.learningInsightsEnabled!==true/,'missing preference must be treated as disabled');
assert.match(app,/robotReadSettings\(\)\.learningInsightsEnabled!==true\)return null/,'idle/context insight snapshot must be gated off by default');
assert.match(app,/robotReadSettings\(\)\.learningInsightsEnabled!==true\)\{streamRobotMessage/,'direct analysis must be gated off by default');
assert.match(app,/const getRobotLearningSnapshot=\(\)=>|function getRobotLearningSnapshot\(\)/,'snapshot provider must remain explicit');
assert.match(app,/buildRobotLearningInsights\(getRobotLearningSnapshot\(\)\)/,'analysis must use an in-memory snapshot only');
assert.match(app,/function clearRobotProgressDashboards\(\)/,'disabling insights must clear visible progress dashboards');
assert.match(app,/if\(!nextEnabled\)clearRobotProgressDashboards\(\)/,'turning insights off must remove visible progress snapshots');
assert.match(app,/robot-progress-dashboard.*remove/,'dashboard cleanup must remove rendered progress cards');
console.log('PASS: Robot Buddy insights are opt-in; engines are storage/network-free; snapshot analysis is local and read-only.');
