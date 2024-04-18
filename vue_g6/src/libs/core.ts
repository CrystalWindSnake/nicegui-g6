export function getExtractEventObjectFn(args: string[] | string) {
  if (Array.isArray(args)) {
    return (obj: Record<string, any>) => {
      let extractedValues = {} as any;
      if (args.length > 0) {
        args.forEach((key) => {
          extractedValues[key] = obj[key];
        });
      } else {
        extractedValues = obj;
      }

      return extractedValues;
    };
  } else if (typeof args === "string") {
    // args like "(ev) => ({...ev})"

    return new Function("obj", `return (${args})(obj)`);
  } else {
    throw new Error("Invalid arguments for extractEventObject");
  }
}
