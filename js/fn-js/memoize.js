const memoize = (f) => {

	const cache = {};

	return (...args) => {

		const argStr = JSON.stringify(args);
		cache[argStr] = cache[argStr] || f(...args);
		return cache[argStr];
	};
};

// Example of simplification of pure functions using Map from immutablejs
// p - player, a - attacker, t - target
const { Map } = require('immutable');

const joe = Map({name: 'joe', hp: 20});
const jack = Map({name: 'jack', hp: 20});

const decrementHP = p => p.set('hp', p.get('hp') - 1);
const isSameTeam = (p1, p2) => p1.get('team') === p2.get('team');
const punch = (a,t) => (isSameTeam(a,t) ? t : decrementHP(t));

punch(joe, jack)
