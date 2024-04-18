import { expect, assert, describe, it } from "vitest";
import { getExtractEventObjectFn } from "./core";

describe("test getExtractEventObjectFn", () => {
  it("extractEventObject should work by list args", () => {
    const event = {
      a: 1,
      b: 2,
      c: 3,
    };

    const result = getExtractEventObjectFn(["a", "b"])(event);
    expect(result).toStrictEqual({
      a: 1,
      b: 2,
    });
  });

  it("extractEventObject should work by string args", () => {
    const event = {
      a: 1,
      b: 2,
      c: 3,
      d: {
        e: 4,
        f: 5,
      },
    };

    const fn = "obj=> ({a:obj.a,e:obj.d.e})";
    const result = getExtractEventObjectFn(fn)(event);
    expect(result).toStrictEqual({
      a: 1,
      e: 4,
    });
  });
});
