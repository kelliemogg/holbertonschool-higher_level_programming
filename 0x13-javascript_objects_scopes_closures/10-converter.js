#!/usr/bin/node
exports.converter = function (base) {
  return function (baseOther) {
    return (parseInt(baseOther).toString(base));
  };
};
